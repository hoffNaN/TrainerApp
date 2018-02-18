from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post, BasicUser, Trainer, GymOwner
from .serializers import PostSerializer, BasicUserSerializer, TrainerSerializer, GymOwnerSerializer


class PostView(APIView):

    def get(self, request):
        Posts = Post.objects.all()
        serializer = PostSerializer(Posts, many=True)
        return Response(serializer.data)

class BasicUserView(APIView):

    def get(self,request):
        BasicUsers = BasicUser.objects.all()
        serializer = BasicUserSerializer(BasicUsers, many=True)
        return Response(serializer.data)

class TrainerView(APIView):

    def get(self,request):
        Trainers = Trainer.objects.all()
        serializer = TrainerSerializer(Trainers, many=True)
        return Response(serializer.data)

class GymOwnerView(APIView):

    def get(self,request):
        GymOwners = GymOwner.objects.all()
        serializer = GymOwnerSerializer(GymOwners, many=True)
        return Response(serializer.data)
