from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from book_service.models import Book
from book_service.serializers import BookSerializer


BOOK_URL = reverse("book_service:book-list")
SAMPLE_BOOK_DATA = {
        "title": "Sample book",
        "author": "Test Author",
        "cover": "H",
        "inventory": 6,
        "daily_fee": 10.00,
    }


def sample_book(**params):
    defaults = SAMPLE_BOOK_DATA.copy()
    
    defaults.update(params)

    return Book.objects.create(**defaults)

def detail_url(book_id):
    return reverse("book_service:book-detail", args=[book_id])


class PublicTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_books_list(self):
        sample_book()
        sample_book()

        res = self.client.get(BOOK_URL)

        books = Book.objects.order_by("id")
        serializer = BookSerializer(books, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_book_detail(self):
        book = sample_book()
        serializer = BookSerializer(book)

        res = self.client.get(detail_url(book.id))

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)


    def test_book_create_not_allowed(self):
        res = self.client.post(
            BOOK_URL,
            data=SAMPLE_BOOK_DATA
        )
        print(res.status_code)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            "test@test.com", "testpass"
        )
        self.client.force_authenticate(self.user)

    def test_book_create_not_allowed(self):
        res = self.client.post(
            BOOK_URL,
            data=SAMPLE_BOOK_DATA
        )

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)


class AdminTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            "admin@admin.com", "testpass", is_staff=True
        )
        self.client.force_authenticate(self.user)

    def test_book_create(self):
        res = self.client.post(
            BOOK_URL,
            data=SAMPLE_BOOK_DATA
        )

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
