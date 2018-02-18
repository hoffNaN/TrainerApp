from trainer.models import Post, BasicUser, Trainer, GymOwner
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
