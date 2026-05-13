from rest_framework.viewsets import ModelViewSet

from book_service.models import (
    Book,
)
from book_service.serializers import (
    BookSerializer,
)


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
