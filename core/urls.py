from django.urls import path

from .views import UserView, CommentView, ProfileView, VoteList

urlpatterns = [
    path('users/', UserView.as_view(), name='users'),
    path('comments/', CommentView.as_view(), name='comments'),
    path("comments/<int:pk>/votes/", VoteList.as_view(), name="vote_list"),
    path('profiles/', ProfileView.as_view(), name='profiles'),
]