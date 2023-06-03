from django.urls import path
from . import views
from .views import BlogListview, BlogDetailView


urlpatterns = [
    path('', BlogListview.as_view(), name='home'),
    path('blog_detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('about/', views.about, name='about')
]