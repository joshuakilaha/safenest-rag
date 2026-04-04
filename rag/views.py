from rest_framework.decorators import api_view
from rest_framework.response import Response

from .services.generation import generate_answer


@api_view(["POST"])
def chat(request):
    query = request.data.get("query", "").strip()

    if not query:
        return Response({"error": "Query is required."}, status=400)

    result = generate_answer(query)

    return Response(result)