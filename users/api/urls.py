from django.urls import path
from users.api import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('register', views.register_view),
    path('login', obtain_auth_token)
]