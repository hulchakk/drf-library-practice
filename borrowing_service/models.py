from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Q, F

from book_service.models import Book


class Borrowing(models.Model):
    borrow_date = models.DateField()
    expected_return_date = models.DateField()
    actual_return_date = models.DateField(null=True, blank=True)
    book = models.ForeignKey(
        Book,
        related_name="borrowings",
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        get_user_model(),
        related_name="borrowings",
        on_delete=models.CASCADE
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(borrow_date__lt=F("expected_return_date")),
                name="borrow_date_before_expected_return_date"
            ),
            models.CheckConstraint(
                check=Q(borrow_date__lt=F("actual_return_date")),
                name="borrow_date_before_actual_return_date"
            ),
        ]

    def __str__(self):
        return f"{self.user} - {self.borrow_date}: {self.book}"
