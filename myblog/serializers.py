from django.core import serializers
from rest_framework import serializers
from myblog.models import Profile ,Category , UserBlog , Comment , Rating
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    contact_no = serializers.CharField(max_length=200)
    class Meta:
        model = User
        fields = ('email','password','first_name','last_name','contact_no')
        read_only_fields = ('contact_no')
        write_only_fields = ('password')

class EmailVerifySerializer(serializers.Serializer):
    email = serializers.EmailField()

class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)

    
    class Meta:
        model=Profile
        fields = ('email','password','gender','contact', 'image', 'created_at',)
        # fields = ('name',)
        read_only_fields = ('created_at')
        write_only_fields = ('password',)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields = ('id','name')

class UserBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserBlog
        fields = ('id','title', 'category', 'description')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields = ('id','user','blog', 'description')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rating
        fields = ('id','user','blog', 'rating')