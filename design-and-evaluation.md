
# Design-and-evaluation.md

```md
# Design and Evaluation

## 1. System Design

The system follows a Retrieval-Augmented Generation (RAG) architecture.

### Architecture Flow
1. Documents are ingested and converted into embeddings
2. Stored in Chroma vector database
3. User query is converted into embedding
4. Relevant documents retrieved
5. AI model generates response

---

## 2. Design Decisions

### Use of RAG
RAG was chosen to ensure responses are grounded in real company data and reduce hallucination.

### Django Backend
Chosen for:
- Rapid development
- Strong API support
- Scalability

### Chroma Vector Database
Chosen because:
- Lightweight
- Easy local persistence
- Good integration with LangChain

### Groq LLM
Chosen for:
- Fast inference
- Low cost compared to OpenAI/OpenRouter/ Cohere
- High performance

### HuggingFace Embeddings
Used to convert text into numerical vectors for similarity search.

---

## 3. Evaluation Approach

Evaluation was conducted using qualitative testing.

### Method:
- Asked multiple real-world questions
- Compared responses with source documents
- Checked relevance and correctness

### Example Questions:
- What data must be encrypted?
- What is the remote work policy?

---

## 4. Results

- Responses were accurate and relevant
- System successfully retrieved correct document sections
- Minimal hallucination observed

---

## 5. Limitations

- No quantitative metrics (precision/recall)
- Dependent on document quality
- Performance limited by model loading time

---

## 6. Future Improvements

- Add evaluation metrics
- Improve response speed
- Add user feedback system