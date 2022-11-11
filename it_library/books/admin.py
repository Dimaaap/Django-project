from django.contrib import admin
from .models import Book, Author, Category


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'get_categories', 'get_authors', 'price', 'image')
    list_display_links = ('id', 'title')
    search_field = ('title', 'get_categories', 'get_authors')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'biography')
    list_display_links = ('id', 'fullname')
    search_fields = ('fullname',)


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
