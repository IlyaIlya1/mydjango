from django.contrib import admin
from .models import Review, Category


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'created_at', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']


admin.site.register(Review, ReviewAdmin)
admin.site.register(Category, CategoryAdmin)
