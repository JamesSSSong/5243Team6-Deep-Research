# Deep Researcher Pipeline

## Introduction
We will extend the existing pipeline (web + YouTube) by:
- Adding **Reddit** as a third retrieval source  
- Persisting all text and metadata in **MongoDB**  
- Indexing semantic vectors in **Pinecone** for fast, focused recall  
- Pushing final summaries into a **Microsoft Teams** channel  

This will improve **breadth** (community insights), **traceability** (raw archive), and **precision** (semantic search), while surfacing results directly in your team’s collaboration hub.

## Objectives
- **O1:** Integrate Reddit search (posts + comments) into the “generate → fetch → store” loop  
- **O2:** Architect a MongoDB schema to hold raw text + metadata from web, YouTube, and Reddit  
- **O3:** Build an embedding & upsert pipeline to Pinecone for vector search  
- **O4:** Enhance the `reflect_on_summary` step to pull top k semantically related chunks from Pinecone  
- **O5:** Replace the email deliverable with a Teams‑message deliverable (via webhook or Graph API)  
- **O6 (Bonus):** Update the LangGraph data model to represent Reddit nodes and cross‑links  
