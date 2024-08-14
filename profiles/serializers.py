from rest_framework import serializers
from .models import Profile


# just like forms 

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Profile

        # for fields we can either use '__all__' to show all fields or just specify the field we want in the Get response
        #fields = '__all__'
        fields = [
            'id','owner','created_at','updated_at', 'name', 'content', 'image'
        ]
        # now include this serializer class in the Profile