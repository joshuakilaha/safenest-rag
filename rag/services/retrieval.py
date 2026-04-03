from pathlib import Path

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


BASE_DIR = Path(__file__).resolve().parent.parent.parent
CHROMA_DIR = BASE_DIR / "chroma_db"


def get_embedding_model():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


def get_vectorstore():
    embeddings = get_embedding_model()

    return Chroma(
        persist_directory=str(CHROMA_DIR),
        embedding_function=embeddings,
    )


def retrieve_documents(query, k=3):
    vectorstore = get_vectorstore()
    results = vectorstore.similarity_search(query, k=k)

    formatted_results = []
    for doc in results:
        formatted_results.append(
            {
                "content": doc.page_content,
                "source": doc.metadata.get("source"),
                "title": doc.metadata.get("title"),
            }
        )

    return formatted_results