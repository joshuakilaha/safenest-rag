from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .services.generation import generate_answer

def chat_page(request):
    return render(request, "rag/chat.html")


@api_view(["POST"])
def chat(request):
    query = request.data.get("query", "").strip()

    if not query:
        return Response({"error": "Query is required."}, status=400)

    result = generate_answer(query)

    return Response(result)