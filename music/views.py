from django.http import HttpResponse
from django.http import Http404
from .models import Artist , Song
from django.shortcuts import render , get_object_or_404
from  rest_framework.views import APIView
from  rest_framework.response import Response
from  rest_framework import status
from .serializers import ArtistSerializer

# Create your views here.


# List all artists or create a new one
#artists/
class ArtistList(APIView) :

    def get(self , request):
        artist = Artist.objects.all()
        serializer = ArtistSerializer(artist , many=True)
        return Response(serializer.data)


    def post(self):
        pass














