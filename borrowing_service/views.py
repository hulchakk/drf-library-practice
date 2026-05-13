from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin

from borrowing_service.serializers import BorrowingSerializer, BorrowingDetailSerializer
from borrowing_service.models import Borrowing


class BorrowingViewSet(GenericViewSet, RetrieveModelMixin, ListModelMixin):
    queryset = Borrowing.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return BorrowingDetailSerializer
        if self.action == "list":
            return BorrowingSerializer
