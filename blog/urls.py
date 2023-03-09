from django.urls import path
from . import views as blog_views
import users.views as user_views
from .views import PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    # using a variable in the route (for individual posts, which will be numbered)
    # the detail view is expecting the "pk" variable (we could change this in the class)
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', blog_views.about, name='blog-about'),
]

