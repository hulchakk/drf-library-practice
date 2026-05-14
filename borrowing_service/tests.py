import uuid

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from borrowing_service.models import Borrowing
from book_service.tests import sample_book
from borrowing_service.serializers import BorrowingSerializer


BORROWING_URL = reverse("borrowing_service:borrowing-list")
SAMPLE_BORROWING_DATA = {
    "borrow_date": "2007-01-01",
    "expected_return_date": "2007-02-02",
}


def sample_borrowing(**params):
    data = SAMPLE_BORROWING_DATA.copy()

    if "actual_return_date" in params:
        data["actual_return_date"] = params["actual_return_date"]

    if "user" not in params:
        unique_email = f"user_{uuid.uuid4()}@test.com"
        data["user"] = get_user_model().objects.create_user(
            unique_email, "testpass"
        )

    if "book" not in params:
        data["book"] = sample_book()

    data.update(params)

    return Borrowing.objects.create(**data)


class PublicTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_no_endpoid_allowed(self):
        res = self.client.get(BORROWING_URL)

        self.assertEquals(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            "user@test.com", "testpass"
        )
        self.client.force_authenticate(self.user)

    def test_borrowing_list(self):
        sample_borrowing()
        user_borrowing = sample_borrowing(user=self.user)

        res = self.client.get(BORROWING_URL)

        serializer = BorrowingSerializer(user_borrowing)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual([serializer.data], res.data)

    def test_create_borrowing(self):
        data = SAMPLE_BORROWING_DATA.copy()
        data["book"] = sample_book().id

        res = self.client.post(
            BORROWING_URL,
            data=data,
        )

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Borrowing.objects.count(), 1)

    def test_filter_active_borrowing(self):
        sample_borrowing(
            user=self.user,
            actual_return_date="2020-01-01"
        )
        active_borrowing = sample_borrowing(user=self.user)

        res = self.client.get(
            BORROWING_URL,
            data={"is_active":"true"}
        )

        seriazer = BorrowingSerializer(active_borrowing)        

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual([seriazer.data], res.data)
