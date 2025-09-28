from django.contrib import admin
from .models import Book


# Register your models here.
@admin.register(Book)
class BookaAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock", "circulation", "volume", "page_count", "edition", "created_at")
    search_fields = ("name",)
    list_filter = ("edition",)
    prepopulated_fields = {"slug": ("name",)}


