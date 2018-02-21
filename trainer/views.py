from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post, BasicUser, Trainer, GymOwner
from .models import Address, Contact, Gym, Offer, TrainType, Opinion
from .serializers import  BasicUserSerializer, TrainerSerializer, GymOwnerSerializer
from .serializers import AddressSerializer, ContactSerializer, GymSerializer, OfferSerializer
from .serializers import PostSerializer, TrainTypeSerializer, OpinionSerializer
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

class AddressView(APIView):

    def get(self,request):
        Addresses = Address.objects.all()
        serializer = AddressSerializer(Addresses, many=True)
        return Response(serializer.data)

class ContactView(APIView):

    def get(self,request):
        Contacts = Contact.objects.all()
        serializer = ContactSerializer(Contacts, many=True)
        return Response(serializer.data)

class GymView(APIView):

    def get(self,request):
        Gyms = Gym.objects.all()
        serializer = GymSerializer(Gyms, many=True)
        return Response(serializer.data)

class OfferView(APIView):

    def get(self,request):
        Offers = Offer.objects.all()
        serializer = OfferSerializer(Offers, many=True)
        return Response(serializer.data)

class TrainTypeView(APIView):

    def get(self,request):
        TrainTypes = TrainType.objects.all()
        serializer = TrainTypeSerializer(TrainTypes, many=True)
        return Response(serializer.data)

class OpinionView(APIView):

    def get(self,request):
        Opinions = Opinion.objects.all()
        serializer = OpinionSerializer(Opinions, many=True)
        return Response(serializer.data)
