from rest_framework.decorators import api_view
from rest_framework.response import Response

from .services.retrieval import retrieve_documents


@api_view(["POST"])
def chat(request):
    query = request.data.get("query", "").strip()

    if not query:
        return Response({"error": "Query is required."}, status=400)

    results = retrieve_documents(query, k=3)

    return Response({
        "query": query,
        "results": results,
    })