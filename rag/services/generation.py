from langchain_openai import ChatOpenAI

from .retrieval import retrieve_documents


def build_context(results):
    context_parts = []

    for i, item in enumerate(results, start=1):
        context_parts.append(
            f"""Source {i}:
Title: {item.get('title')}
File: {item.get('source')}
Content:
{item.get('content')}
"""
        )

    return "\n\n".join(context_parts)


def format_citations(results):
    citations = []
    seen = set()

    for item in results:
        key = (item.get("title"), item.get("source"))
        if key not in seen:
            seen.add(key)
            citations.append(
                {
                    "title": item.get("title"),
                    "source": item.get("source"),
                }
            )

    return citations


def generate_answer(query):
    retrieved_docs = retrieve_documents(query, k=3)

    if not retrieved_docs:
        return {
            "answer": "I can only answer questions based on the SafeNest policy documents provided.",
            "citations": [],
            "retrieved_docs": [],
        }

    context = build_context(retrieved_docs)

    prompt = f"""
You are an assistant for SafeNest company policies.

Answer the user's question using ONLY the retrieved policy context below.
Rules:
1. If the answer is not clearly supported by the context, say:
   "I can only answer based on the SafeNest policy documents provided."
2. Do not make up information.
3. Keep the answer concise and professional.
4. Include a short citation line at the end using the policy title(s).

User question:
{query}

Retrieved policy context:
{context}
"""

    llm = ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0
    )

    response = llm.invoke(prompt)
    answer_text = response.content.strip()

    return {
        "answer": answer_text,
        "citations": format_citations(retrieved_docs),
        "retrieved_docs": retrieved_docs,
    }