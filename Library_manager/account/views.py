from account.models import User
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser



class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    queryset = User.objects.all().order_by("-created_time")
    serializer_class = UserSerializer
    lookup_field = 'slug'