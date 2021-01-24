from rest_framework import serializers
from .models import Todo,CartItem
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
class TodoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Todo
    fields = ('id', 'title', 'authors', 'completed','rating','isbn', 'languageCode', 'ratingCount', 'price')

class CartItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = CartItem
    fields = ('id', 'product', 'price_ht', 'cart','product')


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
