from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Comment, Profile, Vote

class ProfileSerializer(serializers.ModelSerializer):
    bio = serializers.CharField(required=False)
    address = serializers.CharField(required=False)

    class Meta:
        model = Profile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    profile = ProfileSerializer(read_only=True, required=False)
    
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'age', 'password','profile', )
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, value):
        return value.lower()

    def create(self, validated_data):
        User = get_user_model()
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            age=validated_data['age'],
        )

        user.set_password(validated_data['password'])
        user.save()
        Profile.objects.create(user=user)
        return user
    

class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vote
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Comment
        fields = '__all__'
