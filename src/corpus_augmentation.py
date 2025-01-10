import os
import re

from markdown import markdown
from bs4 import BeautifulSoup


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
    def table_converter(corpus):
        pass
