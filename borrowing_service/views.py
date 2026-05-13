from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin

from borrowing_service.serializers import BorrowingSerializer
from borrowing_service.models import Borrowing


class BorrowingViewSet(GenericViewSet, RetrieveModelMixin, ListModelMixin):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer
