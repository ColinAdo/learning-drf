from django.urls import path

from .views import UserView, CommentView

urlpatterns = [
    path('users/', UserView.as_view(), name='users'),
    path('comments/', CommentView.as_view(), name='comments'),
]