from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Comment, Profile, Vote

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    profile = ProfileSerializer(read_only=True, required=False)
    
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'age', 'profile', )

    def validate_email(self, value):
        return value.lower()
    

class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vote
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Comment
        fields = '__all__'
