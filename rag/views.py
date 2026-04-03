from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services.rag_pipeline import simple_response


@api_view(['POST'])
def chat(request):
    """Handle chat requests and return responses."""
    query = request.data.get("query")
    answer = simple_response(query)
    return Response({"answer": answer})