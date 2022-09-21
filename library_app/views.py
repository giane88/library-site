from django.shortcuts import render
from rest_framework import viewsets

from . import models, serializers

# Create your views here.

class AuthorViewSet (viewsets.ModelViewSet):
    queryset = models.Author.objects.all().order_by('second_name')
    serializer_class = serializers.AuthorSerializer
    
class SagaViewSet (viewsets.ModelViewSet):
    queryset = models.Saga.objects.all().order_by('id')
    serializer_class = serializers.SagaSerializer
    
class BookViewSet (viewsets.ModelViewSet):
    queryset = models.Book.objects.all().order_by('id')
    serializer_class = serializers.BookSerializer