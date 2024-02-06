from django.urls import path

from .views import (
    UserView, 
    UserDetailView, 
    CommentView, 
    ProfileView, 
    VoteList, 
    AccountView,
    AccountDetailView
)

urlpatterns = [
    path('users/', UserView.as_view(), name='users'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:pk>/profile/', ProfileView.as_view(), name='users'),
    path('comments/', CommentView.as_view(), name='comments'),
    path("comments/<int:pk>/votes/", VoteList.as_view(), name="vote_list"),
    path('accounts/', AccountView.as_view(), name='accounts'),
    path('accounts/<int:pk>/', AccountDetailView.as_view(), name='account-detail'),

]