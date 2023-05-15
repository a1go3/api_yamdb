from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from reviews.models import Review, Titles
from .serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_title(self):
        return get_object_or_404(Titles, id=self.kwargs.get('title_id'))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, title=self.get_title())

    def get_queryset(self):
        return Review.objects.filter(title=self.get_title())