from django.contrib import admin
from django.urls import path
from trainer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', views.PostView.as_view()),
]
