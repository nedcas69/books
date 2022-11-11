from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from store.models import Book
from store.permissions import IsOwnerOrReadOnly
from store.serializers import BookSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend



class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsOwnerOrReadOnly]
    filter_fields = ['price']
    search_fields = ['name', 'author_name']
    ordering_fields = ['price', 'name']
    
    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()
   
    
def auth(request):
    return render(request, 'oauth.html')

