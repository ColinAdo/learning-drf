from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Comment

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'age', )

    def validate_email(self, value):
        return value.lower()
    
class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = '__all__'
