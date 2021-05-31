from re import I

from rest_framework import serializers

from .models import Album, Images


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['id', 'name', 'url']


class AlbumSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    images=serializers.SlugRelatedField(many=True,slug_field='url',read_only=True)

    class Meta:
        model = Album
        fields = ('id', 'name', 'images')


class AddAlbumSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)


    class Meta:
        model = Album
        fields = ('id', 'name', 'images')


class EditAlbumSerializer(serializers.ModelSerializer):
    # images = ImagesSerializer(many=True)
    name = serializers.CharField(required=False)

    class Meta:
        model = Album

        fields = ['id', 'name', 'images']

    def update(self, instance, validated_data):
        instance.names = validated_data.get('name', instance.name)
        uservalidateddata = validated_data.pop('images', None)
        for i in uservalidateddata:
            instance.images.add(i)

        instance.save()
        return instance
