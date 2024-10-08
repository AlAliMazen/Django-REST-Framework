from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from django_rest_main_app.permissions import IsOwnerOrReadOnly



# Create your views here.

class ProfileList(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True, context={'request':request})
        return Response(serializer.data)


class ProfileDetail(APIView):
    """
    used to get the profile by its ID
    """

    # to have a nice form we just need the serilaizer profile instance
    serializer_class = ProfileSerializer

    # initialize the class of permission
    permission_classes = [IsOwnerOrReadOnly]

    # gets profile with its ID and raise a 404 error when it doesn't exist.
    def get_object(self, pk):
        try:
            profile = Profile.objects.get(pk=pk)
            self.check_object_permissions(self.request, profile)
            return profile
        except Profile.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, context={'request':request})
        return Response(serializer.data)
    
    # to update the profile of auser we need to write a method as folllowing
    def put(self, request, pk):
        # 1st- get the profile we need to update
        # check if the new data are valid
        # if valid save 
        # otherwise return error
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)