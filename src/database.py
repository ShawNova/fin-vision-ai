import os
import json
import logging
from typing import List, Dict, Any, Optional

import lancedb
from lancedb.pydantic import Vector, LanceModel

class CorpusItem(LanceModel):
    doc_id: str
    find_id: str
    title: str
    text: str
    vector: Vector(2)


class DBService:
    """
    A service class to handle operations on LanceDB for a RAG pipeline.
    """
    def __init__(self, db_path: str, table_name: str, schema, is_table_new: bool = False):
        self.db_path = db_path
        self.table_name = table_name
        if not os.path.exists(self.db_path):
            os.makedirs(self.db_path)  # TODO: a system permission issue
        self.db = lancedb.connect(self.db_path)
        if self.table_name in self.db.table_names():
            if is_table_new:
                self.db.drop_table(self.table_name)
                self.table = self.db.create_table(self.table_name, schema=schema)
            else:
                self.table = self.db.open_table(self.table_name)
        else:
            self.table = self.db.create_table(self.table_name, schema=schema)

    def add_documents(self, corpus: List[Dict[str, Any]], batch_size: int = 1) -> None:
        n_corpus = len(corpus)
        for i in range(0, len(corpus), batch_size):
            batch = corpus[i:i+batch_size]
            self.table.add(
                data=[
                    {
                        "doc_id": doc_id,
                        "find_id": doc_id,
                        "title": doc_title,
                        "text": doc_text
                    } for doc_id, doc_title, doc_text in batch
                ]
            )





if __name__ == "__main__":
    # test
    db = DBService(
        db_path="./database/lancedb",
        table_name="test"
    )