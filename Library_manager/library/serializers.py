from . import models
from rest_framework import serializers



class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = "__all__"
        read_only_fields = ['id', 'slug']

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Publisher
        fields = "__all__"
        read_only_fields = ['id', 'slug']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Publisher
        fields = "__all__"
        read_only_fields = ['id', 'slug']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = "__all__"
        read_only_fields = ['id', 'slug', 'isbn']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transaction
        fields = "__all__"
        read_only_fields = ['id']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = "__all__"
        read_only_fields = ['id']