from rest_framework import serializers
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('title',)
