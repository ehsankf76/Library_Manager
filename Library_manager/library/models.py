from django.db import models
from django.conf import settings

# Create your models here.
"""
Me: Category - Book
GPT: Author - Publisher - Transaction - Genre(Category) - Review
"""

class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    genres = models.ManyToManyField(Genre)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Transaction(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_borrowed = models.DateField()
    due_date = models.DateField()

    def __str__(self):
        return f"{self.book.title} - {self.borrower.username}"

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.book.title} - {self.reviewer.username}"
