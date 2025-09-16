from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Текст статьи")
    created_date = models.DateTimeField(auto_now_add=True)

    def get_excerpt(self):
        return self.text[:140] + '...' if len(self.text) > 140 else self.text

    def __str__(self):
        return self.title