from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ModelViewSet

from book_service.models import Book
from borrowing_service.serializers import BorrowingSerializer, BorrowingDetailSerializer
from borrowing_service.models import Borrowing


class BorrowingViewSet(ModelViewSet):
    queryset = Borrowing.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        is_active = self.request.query_params.get("is_active")

        if is_active == "true":
            queryset = queryset.filter(actual_return_date__isnull=True)
        elif is_active == "false":
            queryset = queryset.filter(actual_return_date__isnull=False)

        if not self.request.user.is_staff:
            queryset = queryset.filter(user=self.request.user)
        else:
            user_id = self.request.query_params.get("user_id")

            if user_id:
                queryset = queryset.filter(user_id=user_id)

        return queryset

    def get_serializer_class(self):
        if self.action == "retrieve":
            return BorrowingDetailSerializer
        return BorrowingSerializer

    def perform_create(self, serializer):
        book = serializer.validated_data["book"]

        if book.inventory <= 0:
            raise ValidationError("No book")

        book.inventory -= 1
        book.save()
        serializer.save(user=self.request.user)
