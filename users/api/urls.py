from django.urls import path
from users.api import views


urlpatterns = [
    path('register', views.register_view)
]