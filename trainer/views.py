from rest_framework.views import APIView
 from rest_framework.response import Response
 from .serializers import PostSerializer

 class PostView(APIView):

 def get(self, request):
    Post = Post.objects.all()
    serializer = PostSerializer(Post, many=True)
    return Response(serializer.data)
