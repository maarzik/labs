from django.contrib import admin
from django.urls import path
from helloapp import views  # импортируем наше представление

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello, name='home'),       # маршрут для главной страницы /
    path('hello/', views.hello, name='hello') # маршрут для страницы /hello/
]