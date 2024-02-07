from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Comment, Profile, Vote, Account


class ProfileSerializer(serializers.ModelSerializer):
    bio = serializers.CharField(required=False)
    address = serializers.CharField(required=False)

    class Meta:
        model = Profile
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    profile = ProfileSerializer(required=False, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'age', 'password', 'profile', )
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ['profile']

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
        # depth = 1


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    User = get_user_model()
    url = serializers.HyperlinkedIdentityField(
        view_name='account-detail',
    )
    user = serializers.HyperlinkedRelatedField(
        queryset=User.objects.all(),
        view_name='user-detail',
    )

    class Meta:
        model = Account
        fields = ['url', 'id', 'account_name', 'user', 'created_at']
        depth = 1
        
