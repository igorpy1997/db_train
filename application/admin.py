from django.contrib import admin
from .models import Author, Publisher, Book, Store


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "age")

    def __str__(self):
        return self.name


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ("name",)

    def __str__(self):
        return self.name


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("name", "pages", "price", "rating", "publisher", "pubdate")
    list_filter = ("publisher", "pubdate")
    search_fields = ("name", "publisher__name")
    filter_horizontal = ("authors",)
    date_hierarchy = "pubdate"

    def __str__(self):
        return self.name


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    filter_horizontal = ("books",)

    def __str__(self):
        return self.name
