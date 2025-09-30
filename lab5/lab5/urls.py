from django.contrib import admin
from django.urls import path
from hello import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('postuser/', views.postuser, name='postuser'),
    path('form/', views.form_index, name='form_index'),
]