from django.urls import path
from . import views
from users.views import UserRegistrationAPIView

urlpatterns = [
    path('categories/', views.CategoryListCreateAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail'),
    path('posts/', views.PostListAPIView.as_view(), name='post-list'),
    path('posts/last-week-popular/', views.LastWeekPopularPostListAPIView.as_view(), name='post-last-week-popular'),
    path('posts/last-month-popular/', views.LastMonthPopularPostListAPIView.as_view(), name='post-last-month-popular'),
    path('posts/new/', views.NewPostListAPIView.as_view(), name='new-posts'),
    path('posts/most-seen/', views.MostSeenPostListAPIView.as_view(), name='most-seen'),
    path('posts/recommended/', views.RecommendedPostListApiView.as_view(), name='recommends'),
    path('posts/create/', views.PostCreateAPIView.as_view(), name='post-create'),
    path('posts/<int:pk>/', views.PostRetrieveAPIView.as_view(), name='post-detail'),
    path('comment/create/', views.CommentCreateAPIView.as_view(), name='comment-list'),
    path('register/', UserRegistrationAPIView.as_view(), name='user-registration'),
]
