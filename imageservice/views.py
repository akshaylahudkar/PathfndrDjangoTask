from django.shortcuts import render
from rest_framework import generics, response, status
# Create your views here.
# views.py
from rest_framework import viewsets

from .serializers import ImagesSerializer, AlbumSerializer, EditAlbumSerializer, AddAlbumSerializer
from .models import Images, Album


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all().order_by('name')
    serializer_class = AlbumSerializer


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all().order_by('name')
    serializer_class = ImagesSerializer


class AddImageAPI(generics.GenericAPIView):
    serializer_class = ImagesSerializer

    def post(self, request, *kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        image = serializer.save()
        return response.Response({"image": ImagesSerializer(image, context=self.get_serializer_context()).data})


class AddAlbumAPI(generics.GenericAPIView):
    serializer_class = AddAlbumSerializer

    def post(self, request, *kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        album = serializer.save()
        return response.Response({"album": AlbumSerializer(album, context=self.get_serializer_context()).data})


class editAlbumAPI(generics.GenericAPIView):
    serializer_class = EditAlbumSerializer

    def put(self, request, pk, format=None):
        device = Album.objects.get(id=pk)
        serializer = EditAlbumSerializer(device, data=request.data)

        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.update(device, serializer.validated_data)

            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
