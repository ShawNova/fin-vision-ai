import openai

class SysPrompts:
    table_convert_instructions = """The following text contains a table that may not follow standard Markdown formatting. Extract the table's content, identify headers and rows clearly, explain the meanings, output plain text. If headers are not the first line, infer the headers based on the content."""

    query_expansion = "Expand the following query with semantic relevant synonyms and terms to generate a richer query.  Please return in sentences."

class ChatClient:
    @staticmethod
    def get_first_response_from_openai(client, model_name, system_prompt=None, user_prompt=None, max_tokens=200, temperature=0):
        response = ""
        try:
            resp = client.chat.completions.create(
                model=model_name,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                max_tokens=max_tokens,
                temperature=temperature
            )
            response = resp.choices[0].message.content
        except Exception as err:
            print(err)
        return response






