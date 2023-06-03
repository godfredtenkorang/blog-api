from django.urls import path
from blog.api import views

urlpatterns = [
    path('', views.blog_view),
    path('<int:pk>/', views.blog_detail_view),
    path('<int:pk>/update', views.blog_update_view),
    path('<int:pk>/delete', views.blog_delete_view),
    path('create', views.blog_create_view),
]