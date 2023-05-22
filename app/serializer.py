from rest_framework import serializers
from .models import Recipie,Favorite,Comment

class RecipieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipie
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        
