from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer


class PostView(APIView):

    def get(self, request):
        Posts = Post.objects.all()
        serializer = PostSerializer(Posts, many=True)
        return Response(serializer.data)
