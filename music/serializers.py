from rest_framework import serializers
from .models import Artist,Song

class ArtistSerializer(serializers.ModelSerializer) :

    class Meta :
        model = Artist
        #fields = ('artist' , 'artist_photo')
        #or
        fields = '__all__'