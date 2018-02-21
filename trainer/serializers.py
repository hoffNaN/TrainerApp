from trainer.models import Post, BasicUser, Trainer, GymOwner
from trainer.models import  Address, Contact, Gym, Offer, TrainType, Opinion
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=False)

    class Meta:
        model = Post
        fields = ('author', 'title', 'text', 'created_date','published_date')

class BasicUserSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)

    class Meta:
        model = BasicUser
        fields = ('user', 'name', 'dayofbirth', 'interests','contact','discription','sex','address','trainer','gymowner')

class TrainerSerializer(serializers.ModelSerializer):
    qualifications = serializers.StringRelatedField(many=False)

    class Meta:
        model = Trainer
        fields = ('qualifications','gym','experience','specialization','rating','offert')

class GymOwnerSerializer(serializers.ModelSerializer):
    gym = serializers.StringRelatedField(many=False)

    class Meta:
        model = GymOwner
        fields = ('gym','offert')

class AddressSerializer(serializers.ModelSerializer):
    country_code = serializers.StringRelatedField(many=False)

    class Meta:
        model = Address
        fields = ('country','province','city')

class ContactSerializer(serializers.ModelSerializer):
    country_code = serializers.StringRelatedField(many=False)

    class Meta:
        model = Contact
        fields = ('phone','email','fb')

class GymSerializer(serializers.ModelSerializer):
    name_gym = serializers.StringRelatedField(many=False)

    class Meta:
        model = Gym
        fields = ('name_gym','discription','contact','offert')

class OfferSerializer(serializers.ModelSerializer):
    discription = serializers.StringRelatedField(many=False)

    class Meta:
        model = Offer
        fields = ('discription','price','train_type','localization')

class TrainTypeSerializer(serializers.ModelSerializer):
    discription = serializers.StringRelatedField(many=False)

    class Meta:
        model = TrainType
        fields = ('train_type')

class OpinionSerializer(serializers.ModelSerializer):
    discription = serializers.StringRelatedField(many=False)

    class Meta:
        model = Opinion
        fields = ('opinion_type')
