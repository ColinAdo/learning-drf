from django.contrib.auth import get_user_model
from rest_framework import generics

from .serializers import UserSerializer, CommentSerializer, ProfileSerializer, VoteSerializer
from .models import Comment, Profile, Vote

class UserView(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class ProfileView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class VoteList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Vote.objects.filter(comment_id=self.kwargs["pk"])
        return queryset
    serializer_class = VoteSerializer

