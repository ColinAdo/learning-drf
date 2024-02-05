from django.contrib.auth import get_user_model
from rest_framework import generics

from .serializers import UserSerializer, CommentSerializer
from .models import Comment

class UserView(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
