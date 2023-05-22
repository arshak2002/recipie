from django.shortcuts import render
from .models import Recipie,Favorite,Comment
from .serializer import RecipieSerializer,FavoriteSerializer,CommentSerializer

from rest_framework .views import APIView
from rest_framework.response import Response
from rest_framework .permissions import IsAuthenticated


# Create your views here.

class ListCreate(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        recipie = Recipie.objects.all()
        serializer = RecipieSerializer(recipie,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        title = request.data.get('title')
        description = request.data.get('description')
        image = request.data.get('image')
        ingrediance = request.data.get('ingrediance')
        instruction = request.data.get('instruction')
        cooking_time = request.data.get('cooking_time')
        data = {
            "user":request.user.id,
            "title":title,
            "description":description,
            "image":image,
            "ingrediance":ingrediance,
            "instruction":instruction,
            "cooking_time":cooking_time
        }
        serializer = RecipieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message":"Created"
                }
            )
        return Response(serializer.errors)
    
class GetItem(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,id):
        item = Recipie.objects.get(id=id)
        serializer = RecipieSerializer(item)
        return Response(serializer.data)
    
    def put(self,request,id):

        item = Recipie.objects.get(id=id)
        if request.user == item.user:

            if 'title' in request.data:
                item.title=request.data.get('title')
            if 'description' in request.data:
                item.description=request.data.get('description')
            if 'image' in request.data:
                item.image=request.data.get('image')
            if 'ingrediance' in request.data:
                item.ingrediance=request.data.get('ingrediance')
            if 'instruction' in request.data:
                item.instruction=request.data.get('instruction')
            if 'cooking_time' in request.data:
                item.cooking_time=request.data.get('cooking_time')

            item.save()
            return Response(
                {
                    "message":"Updated"
                }
            )
        return Response(
            {
                "message":"You have no permission"
            }
        )
    def delete(self,request,id):
        item = Recipie.objects.get(id=id)
        if request.user == item.user:
            item.delete()
            return Response(
                {
                    "message":"Updated"
                }
            )
        
        return Response(
            {
                "message":"You have no permission"
            }
        )

class Search(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        search = request.data.get('search')
        result = Recipie.objects.filter(title__icontains=search)
        if result.count() > 0:
            serializer = RecipieSerializer(result,many=True)
            return Response(serializer.data)
        return Response(
            {
                "message":"No result found"
            }
        )
    
class MyFavorite(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        item_id = request.data.get('item_id')
        item = Recipie.objects.get(id=item_id)
        data = {
            "user":request.user.id,
            "recipie":item.id
        }
        serializer = FavoriteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message":"added to favorite"
                }
            )
        return Response(serializer.errors)
    
    def get(self,request):
        favorite = Favorite.objects.filter(user=request.user)
        serializer = FavoriteSerializer(favorite,many=True)
        return Response(serializer.data)
    
class RatingAndComment(APIView):

    permission_classes = [IsAuthenticated]


    def post(self,request,id):
        comment = request.data.get('comment')
        rating = request.data.get('rating')
        item = Recipie.objects.get(id=id)
        data = {
            "user":request.user.id,
            "recipie":item.id,
            "comment":comment,
            "rating":rating
        }
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def get(self,request,id):
        item = Recipie.objects.get(id=id)
        comment = Comment.objects.filter(recipie=item)
        serializer = CommentSerializer(comment,many=True)
        return Response(serializer.data)










