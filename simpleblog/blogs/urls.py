from django.urls import path
from .views import HomeView, BlogView, CreateBlogView

urlpatterns = [
    path('', HomeView.as_view(), name='blog-home'),
    path('blog/<int:pk>/', BlogView.as_view(), name='detail'),
    path('create_blog/', CreateBlogView.as_view(success_url='/'), name="create_blog")
]
