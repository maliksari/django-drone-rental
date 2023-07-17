from rest_framework import serializers

from app.models import Category
from app.serializers.compressors import ImageCompressor


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'category_code', 'description', 'image')

    def create(self, validated_data):
        image = validated_data.get('image', None)
        if image:
            compressor = ImageCompressor()
            compressed_images = compressor.compress(image)
            if compressed_images:
                validated_data['image'] = compressed_images['original']

        return super().create(validated_data)
