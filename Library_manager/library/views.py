from django.shortcuts import render

# Create your views here.
from rest_framework.parsers import MultiPartParser
from . import permissions
from . import models
from django.shortcuts import get_object_or_404
from . import serializers
from rest_framework import viewsets



class AuthorViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing author instances.
    """
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.IsAdminOrReadOnly]

class PublisherViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing publisher instances.
    """
    queryset = models.Publisher.objects.all()
    serializer_class = serializers.PublisherSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.IsAdminOrReadOnly]

class GenreViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing genre instances.
    """
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.IsAdminOrReadOnly]

class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing book instances.
    """
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    lookup_field = 'slug'

class TransactionViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing transaction instances.
    """
    queryset = models.Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer
    permission_classes = [permissions.TransactionPermission]

class ReviewViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing review instances.
    """
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer