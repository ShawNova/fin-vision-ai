import os
import spacy
from prompt import SysPrompts, ChatClient

class QueryAugment:
    def __init__(self):
        try:
            # Try to load the model
            self.nlp = spacy.load("en_core_web_sm")
        except OSError:
            # If the model is not installed, download it
            print("Downloading 'en_core_web_sm' model...")
            from spacy.cli import download
            download("en_core_web_sm")
            # Load the model after downloading
            self.nlp = spacy.load("en_core_web_sm")

    def decompose_query(self, query):
        """
        Decomposes a complex query into smaller components using SpaCy's noun chunks.
        """
        doc = self.nlp(query)
        sub_queries = [chunk.text for chunk in doc.noun_chunks]
        return sub_queries

    def expand_query(self, query, client=None):
        sub_queries = self.decompose_query(query)
        user_prompt = f"""The original query is: "{query}"."""
        if sub_queries:
            user_prompt = user_prompt + f"""The keywords of the query are "{','.join([x for x in sub_queries])}"."""
        if client:
            print(f"{user_prompt}")
            response = ChatClient.get_first_response_from_openai(
                client=client,
                model_name=os.getenv("OPENAI_MODEL_QUERY_EXPANSION"),
                system_prompt=SysPrompts.query_expansion,
                user_prompt=user_prompt,
                max_tokens=250,
                temperature=0.2 # for creativity
            )
            if response:
                query = f"{query}. {response}"
        return query



