from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer


# Create your views here.
class PostList(APIView):
    """
    to list all the available posts 
    """
    # use serializer class to get a nice form
    serializer_class= PostSerializer

    # check if the user is logged in and authenticated in order to write a post.
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    
    def get(self, request):
        post = Post.objects.all()
        serializer=PostSerializer(
            post, many=True, context={"request":request}
        )
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PostSerializer(
            data=request.data, context = {"request":request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

