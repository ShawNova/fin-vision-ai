import os
import re

from markdown import markdown
from bs4 import BeautifulSoup

from prompt import SysPrompts


class CorpusAugment:
    @staticmethod
    def clean_markdown(text):
        # Remove links: [text](url)
        text = re.sub(r'\[.*?\]\(.*?\)', '', text)
        # Remove inline code: `code`
        text = re.sub(r'`.*?`', '', text)
        # Remove images: ![alt](url)
        text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
        # Remove block quotes: > text
        text = re.sub(r'^>.*', '', text, flags=re.MULTILINE)
        # Remove headings: # Heading
        text = re.sub(r'^#+ ', '', text, flags=re.MULTILINE)
        # Remove bold/italic: **text**, *text*
        text = re.sub(r'\*\*.*?\*\*', '', text)
        text = re.sub(r'\*.*?\*', '', text)
        # Remove horizontal rules: ---
        text = re.sub(r'^---+', '', text, flags=re.MULTILINE)
        # Remove extra spaces
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    @staticmethod
    def markdown_to_text(md):
        # Convert Markdown to HTML
        html = markdown(md)
        # Parse HTML and extract plain text
        soup = BeautifulSoup(html, "html.parser")
        return soup.get_text()

    @staticmethod
    def clean_text(text):
        # clean markdown
        text = CorpusAugment.clean_markdown(text)
        text = CorpusAugment.markdown_to_text(text)
        # clean unicode and punctuation
        text = text.encode('utf-8', 'replace').decode('utf-8', 'replace')
        text = re.sub(r'<\|.*?\|>', '', text)
        text = ' '.join(text.split())
        text = re.sub(r"(\\u[0-9A-Fa-f]{4})+", " ", text)
        text = re.sub("[\"#&*+/:<=>@[\]^_`{|}~]", '', text)
        return text

    @staticmethod
    def truncate_text(text, tokenize_enc_func, tokenize_dec_func, max_chunk_size=8192):
        tokens = tokenize_enc_func(text)
        if len(tokens) > max_chunk_size:
            text = tokenize_dec_func(tokens[:max_chunk_size])
        return text

    @staticmethod
    def extract_markdown_tables(text):
        # Regex pattern to match Markdown tables (handles optional separator rows and last-line edge cases)
        table_pattern = r'((?:\|[^\n]*?\|\n)+(?:\|[-:|\s]*\|\n)?(?:\|[^\n]*?\|(?:\n|$))+)'
        matches = re.findall(table_pattern, text)
        return matches

    @staticmethod
    def markdown_table_to_plaintext(table_text):
        # Convert a standard table to plain text
        lines = table_text.strip().split('\n')
        # check for the row separater
        sep_pattern = r'^\|(?:\s*:?-{2,}:?\s*\|)+$'
        headers = lines[0].strip('|').split('|')
        if len(lines) > 1 and re.match(sep_pattern, lines[1]): # separater is true
            data_rows = lines[2:]
        else:
            data_rows = lines[1:]

        data = [row.strip('|').split('|') for row in data_rows]

        # check table is standard or not
        for row in data:
            if len(headers) != len(row):
                return None

        output = ["There is a table containing the following information:"]
        for row in data:
            row_text = ", ".join(
                f"{header.strip()}: {cell.strip()}" for header, cell in zip(headers, row))
            output.append(f"- {row_text}")

        return "\n".join(output)

    @staticmethod
    def table_converter(text, client=None):
        tables = CorpusAugment.extract_markdown_tables(text)
        tables_converted = []
        text_aug = text
        for table_text in tables:
            # rule-based
            table_text_plain = CorpusAugment.markdown_table_to_plaintext(table_text)
            # gpt-based
            if not table_text_plain and client:
                system_prompt = SysPrompts.table_convert_instructions
                user_prompt = table_text
                resp = client.chat.completions.create(
                    model = os.getenv("OPENAI_MODEL"),
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    max_tokens=500,
                    temperature=0
                )
                table_text_plain = resp.choices[0].message.content
            tables_converted.append(table_text if not table_text_plain else table_text_plain)
        for i in range(len(tables)):
            text_aug = text_aug.replace(tables[i], tables_converted[i])
        return text_aug


