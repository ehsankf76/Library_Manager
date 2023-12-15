from django.contrib import admin
from . import models

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'available')
    list_display_links = ('title',)
    search_fields = ('title', 'author__name', 'publisher__name',)
    list_filter = ('title', 'author', 'publisher', 'genres', 'available')

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)



admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Genre)
admin.site.register(models.Publisher, PublisherAdmin)
admin.site.register(models.Review)
admin.site.register(models.Transaction)