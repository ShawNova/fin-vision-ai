# FinVisionAI: a Financial Q&A system

# Project Overview

The project aims to develop a multimodal AI system that integrates text-to-image and text-to-video capabilities. It will focus on financial services applications, with emphasis on dynamic risk assessment, investment analysis, and personalized user guidance.

# Key Highlights

1. Novel Technique Design:
   - Enhance multimodal generation by incorporating structured data(tables) into ControlNet and Stable Diffusion Model.
2. Achieving SOTA Results
   1. RAG integration: competitive Kaggle benchmark
   2. Multimodality: Target public datasets like TextVQA and COCO Caption for performance benchmarking.
   3. Q&A: Accurate Q&A, dynamic risk visualizations as well as DIY benchmark setting.
3. Business Pipeline Creation
   1. Develop a dynamic service pipeline for financial enterprises.
   2. Design a generative AI-powered educational service for personalized financial learning.
   3. Showcases mastery of cutting-edge techniques like **FAISS**, **LangChain**, and **RAG workflows**.





# Deliverables

1. Kaggle Submission
   - Baseline + optimized model results.
   - Comparison against the leader board.
2. GitHub Repository
   - Clean, modular code showcasing RAG with GPT, Stable Diffusion, and ControlNet.
3. Demo as a Service
   - Show how the solution works in a real-world scenario (e.g., finance Q&A with visual outputs).
   - User input → RAG-enhanced Q&A → Multimodal visual/chart output.
     - **Input**: Users submit financial questions or queries (e.g., “Show my risk profile trends.”).
     - **Output**: Text-based answers with supporting **generated images** or **dynamic charts**.
     - **Backend**
       - **RAG Pipeline**: Retrieves relevant financial insights.
       - **GPT-Based Generation**: Generates explanations or advice.
       - **Multimodal Outputs**: Generates visual charts (e.g., dynamic trendlines) using ControlNet.
     - **Hosting**
       - Deployed as a **cloud-based API** using FastAPI.
       - Accessible via **user-friendly frontend** on AWS or Hugging Face Spaces.
4. Technical Report
   1. Detailing the RAG workflow, knowledge base setup, and retrieval-generation integration.
5. Performance Metrics
   - Improved relevance and accuracy of Q&A responses.
   - [Bonus] Enhanced image quality and context alignment.



# 1-Month Plan

| Week       | Task                                      | Deliverableds                                                |
| ---------- | ----------------------------------------- | :----------------------------------------------------------- |
| **Week 1** | Data Preparation and Model Setup          | - Clean and prepare **financeRAG dataset**. (collecting, cleaning, feature engineering). <br />- Develop RAG pipeline (retrieval + GPT fine-tuning).<br />- Baseline model setup for submission. |
| **Week 2** | Multimodal Core Development + Fine-tuning | -  Integrate RAG with GPT for financial Q&A. <br />- Develop text-to-image generation (ControlNet/Stable Diffusion).. <br />- Perform baseline submissions to Kaggle. |
| **Week 3** | Optimization for Kaggle + Dynamic Visuals | - Tune model hyperparameters to improve competition metrics. <br />- Generate dynamic visualizations conditioned on retrieved data.<br />- Add dynamic chart generation for data visualization. |
| **Week 4** | Integration and Service API Development   | \- Build FastAPI-based backend to serve models (retrieval + generation).<br/>\- Test API endpoints for financial Q&A and multimodal outputs. |
| **Week 5** | Service Deployment and Demo Presentation  | - Deploy the service on **AWS or Hugging Face Spaces**. <br />- Develop a user-friendly interface (Streamlit/Flask). <br />- Prepare demo showcasing real-world commercial viability. |

