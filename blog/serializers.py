from rest_framework import serializers
from blog.models import Category, Post, Comment
from taggit.models import Tag
from django.contrib.auth.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

    class Meta:
        model = User
        fields = ('username', 'password')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id',
            'name',
            'slug'
        )


class PostCreateSerializer(serializers.ModelSerializer):
    tags_id = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), write_only=True)

    class Meta:
        model = Post
        fields = (
            'title',
            'content',
            'category',
            'image',
            'tags_id',
        )


    def create(self, validated_data):
        tags = validated_data.pop('tags_id')
        post = Post.objects.create(tags=tags, **validated_data)
        return post


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.SerializerMethodField()

    def get_post(self, obj):
        return obj.post.title

    class Meta:
        model = Comment
        fields = (
            'comment',
            'post'
        )


class PostSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    tags = TagSerializer(many=True)
    comments = CommentSerializer(many=True)

    def get_category(self, obj):
        return obj.category.title

    class Meta:
        model = Post
        fields = ('id',
                  'created_at',
                  'updated_at',
                  'title',
                  'content',
                  'image',
                  'category',
                  'views',
                  'tags',
                  'comments'

                  )



