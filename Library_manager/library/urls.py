from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter



urlpatterns = [
    
]
router = DefaultRouter()
router.register('authors', views.AuthorViewSet, basename='authors')
router.register('publishers', views.PublisherViewSet, basename='publishers')
router.register('genres', views.GenreViewSet, basename='genres')
router.register('books', views.BookViewSet, basename='books')
router.register('transactions', views.TransactionViewSet, basename='transactions')
router.register('reviews', views.ReviewViewSet, basename='reviews')
urlpatterns += router.urls