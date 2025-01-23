import openai

class SysPrompts:
    table_convert_instructions = """The following text contains a table that may not follow standard Markdown formatting. Extract the table's content, identify headers and rows clearly, explain the meanings, output plain text. If headers are not the first line, infer the headers based on the content."""


