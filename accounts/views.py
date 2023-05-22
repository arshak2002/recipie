from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework .views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# Create your views here.

class Register(APIView):

    def post(self,request):
        username = request.data.get('username')
        first_name = request.data.get('first_name')
        email = request.data.get('email')
        password = request.data.get('password')

        if not User.objects.filter(username=username):
            User.objects.create_user(
                username=username,
                first_name=first_name,
                email=email,
                password=password
            )
            return Response(
                {
                    "message":"User created"
                }
            )
        return Response(
            {
                "message":"This user already exist"
            }
        )
    
class Login(APIView):
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username,password=password)
        if user:
            token,created = Token.objects.get_or_create(user=user)
            return Response(
                {
                    'message':'Login seccussfully',
                    'token':token.key
                }
            )
        return Response(
            {
                'message':'Invalid credentials'
            }
        )

class Logout(APIView):
    def post(self,request):
        request.auth.delete()
        return Response(
            {
            'message':'Logout successfull'
            }
        )


