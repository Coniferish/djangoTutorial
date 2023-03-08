from django.urls import path
from . import views as blog_views
import users.views as user_views
from .views import PostListView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('about/', blog_views.about, name='blog-about'),
]

