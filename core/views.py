from django.contrib.auth import get_user_model
from rest_framework import generics

from .serializers import (
    UserSerializer, 
    CommentSerializer, 
    ProfileSerializer, 
    VoteSerializer,
    AccountSerializer
)


from .models import Comment, Profile, Vote, Account

class UserView(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class ProfileView(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Profile.objects.filter(user_id=self.kwargs['pk'])
        return queryset
    
    serializer_class = ProfileSerializer

class VoteList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Vote.objects.filter(comment_id=self.kwargs["pk"])
        return queryset
    serializer_class = VoteSerializer


class AccountView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
