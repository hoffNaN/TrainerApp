from trainer.models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=False)

    class Meta:
        model = Post
        fields = ('author', 'title', 'text', 'created_date','published_date')
