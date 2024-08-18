from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category
from .serializer import CategorySerializer
from django_rest_main_app.permissions import IsOwnerOrReadOnly
from django.http import Http404

# Create your views here.

class CategoryList(APIView):
    """
    to get a list of available categories
    """
    serializer_class = CategorySerializer

    # check if the user is logged in and authenticated in order to write a post.
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(
            category, many=True, context={"request":request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(
            data = request.data, context={"request":request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

class CategoryDetail(APIView):
    """
    Used to let user update his own category
    """
    serializer_class = CategorySerializer

    # check if the user is logged in and authenticated in order to write a post.
    # initialize the class of permission
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            category = Category.objects.get(pk=pk)
            self.check_object_permissions(self.request, category)
            return category
        except Category.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, context={"request":request})
        return Response(serializer.data)
    
    # to update the profile of auser we need to write a method as folllowing
    def put(self, request, pk):
        # 1st- get the profile we need to update
        # check if the new data are valid
        # if valid save 
        # otherwise return error
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
