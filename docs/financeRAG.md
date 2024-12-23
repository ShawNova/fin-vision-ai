# A Retrieval and Re-Ranking System for FinanceRAG

## Objective

Develop a **retrieval and re-ranking system** to:

1. Retrieve the most relevant document chunks for a given query.
2. Re-rank the retrieved contexts to prioritize relevance based on semantic similarity.

## **Workflow**

### **Step 1: Dataset Preparation**

1. **Corpus**:
   - Use the Kaggle-provided document corpus as the primary dataset for Task 1.
   - If necessary, enrich the corpus with financial text data (e.g., Financial PhraseBank) for domain-specific relevance.
2. **Query and Ground Truth**:
   - Extract queries and their ground truth relevance labels from the competition dataset.
   - Split the dataset into training, validation, and test subsets.
3. **Preprocessing**:
   - Document Chunks
     - Divide long documents into smaller, manageable chunks.
     - Use a fixed chunk size (e.g., 300 words).
   - Embedding Standardization
     - Normalize text embeddings for efficient similarity comparisons.

### Step 2: Retrieval System

1. **Indexing**:
   - Use FAISS (Facebook AI Similarity Search) for fast vector-based retrieval.
   - Encode document chunks using a pre-trained Sentence Transformer (e.g., `all-MiniLM-L6-v2`)
2. **Embedding**: 
   - Convert queries into embeddings using the same Sentence Transformer.
3. **Initial Retrieval**:
   - Use FAISS to retrieve the top-k most similar document chunks.

### Step 3: Re-Ranking System

1. **Relevance Scoring**:
   - Fine-tune a cross-encoder (e.g., `cross-encoder/ms-marco-MiniLM-L-6-v2`) to score query-document pairs for relevance.
2. **Ranking**:
   - Sort the retrieved chunks by relevance scores.
3. **Output Top-N**:
   - Return the top-N most relevant chunks.

### **Step 4: Evaluation**

1. **Metrics**:
   - Use competition-provided metrics like **Precision@k**, **Recall@k**, and **MRR (Mean Reciprocal Rank)** to evaluate retrieval and re-ranking performance.
2. **Validation**:
   - Split the competition dataset into training and validation sets.
   - Evaluate the pipeline on the validation set to optimize parameters.

## Baseline

| Method | Method Info | Performance |
| ------ | ----------- | ----------- |
| BM25   |             |             |
|        |             |             |
|        |             |             |



## Dataset Preparation

Resources

- financial_phrasebank: [takala/financial_phrasebank · Datasets at Hugging Face](https://huggingface.co/datasets/takala/financial_phrasebank)
- FinanceRAG: [Linq-AI-Research/FinanceRAG · Datasets at Hugging Face](https://huggingface.co/datasets/Linq-AI-Research/FinanceRAG?row=1)![image-20241223144017556](E:\personal\projects\fin-vision-ai\docs\figures\image-20241223144017556.png)









