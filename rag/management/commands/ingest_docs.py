from django.core.management.base import BaseCommand
from rag.services.ingest import ingest_documents


class Command(BaseCommand):
    help = "Ingest documents into Chroma vector database"

    def handle(self, *args, **kwargs):
        result = ingest_documents()
        self.stdout.write(self.style.SUCCESS("Documents ingested successfully"))
        self.stdout.write(str(result))