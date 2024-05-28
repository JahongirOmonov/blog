from rest_framework import generics
from .models import Category, Post, Comment
from blog.serializers import CategorySerializer, PostSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from datetime import datetime, timedelta
from django.utils import timezone
from blog import serializers


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all().filter(is_active=True)
    serializer_class = PostSerializer


class NewPostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all().filter(is_active=True).order_by('-created_at')[:5]
    serializer_class = PostSerializer


class MostSeenPostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all().filter(is_active=True).order_by('-views')[:5]
    serializer_class = PostSerializer


class MostWeekPopularPostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all().filter(is_active=True).order_by('-views')[:5]
    serializer_class = PostSerializer


class LastWeekPopularPostListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        one_week_ago = timezone.now() - timedelta(days=7)

        queryset = Post.objects.filter(
            is_active=True,
            created_at__gte=one_week_ago
        ).order_by('-views')
        return queryset[:5]


class LastMonthPopularPostListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        one_month_ago = timezone.now() - timedelta(days=30)

        queryset = Post.objects.filter(
            is_active=True,
            created_at__gte=one_month_ago
        ).order_by('-views')

        return queryset[:5]


class RecommendedPostListApiView(generics.ListAPIView):
    queryset = Post.objects.all().filter(is_recommended=True, is_active=True)
    serializer_class = PostSerializer


class PostRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # Increment the views count
        instance.views += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class PostCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.PostCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class UserRegistrationAPIView(generics.CreateAPIView):
    serializer_class = serializers.UserRegistrationSerializer
