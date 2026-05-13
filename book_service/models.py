from django.db import models


BOOK_COVER_CHOICES = {
    "H": "HARD",
    "S": "SOFT",
}


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    Cover = models.CharField(
        max_length=4,
        choices=BOOK_COVER_CHOICES,
    )
    inventory = models.PositiveIntegerField()
    daily_fee = models.DecimalField(decimal_places=2, max_digits=7)

    def __str__(self):
        return f"{self.title} ({self.author})"
