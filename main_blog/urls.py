# from .views import bloglistview, blogdetailview
from .views import BlogListView, BlogDetailView
from django.urls import path

urlpatterns = [
    path('', BlogListView.as_view(), name='blog-list'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
]