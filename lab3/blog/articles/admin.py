from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date')
    search_fields = ('title', 'text')

admin.site.register(Article, ArticleAdmin)