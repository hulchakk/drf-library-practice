from rest_framework import serializers

from book_service.serializers import BookSerializer
from borrowing_service.models import Borrowing
from user.serializers import UserSerializer


class BorrowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowing
        fields = (
            "id",
            "borrow_date",
            "expected_return_date",
            "actual_return_date",
            "book",
            "user"
        )


class BorrowingDetailSerializer(BorrowingSerializer):
    book = BookSerializer()
    user = UserSerializer()
