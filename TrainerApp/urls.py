from django.contrib import admin
from django.urls import path
from trainer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', views.PostView.as_view()),
    path('basicusers/', views.BasicUserView.as_view()),
    path('trainers/', views.TrainerView.as_view()),
    path('gymowners/', views.GymOwnerView.as_view()),
]
