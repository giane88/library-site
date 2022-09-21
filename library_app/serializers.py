from dataclasses import fields
from rest_framework import serializers
from . import models

class AuthorSerializer (serializers.HyperlinkedModelSerializer):
    """API Endpoint that serialize Author

    Args:
        serializers (_type_): _description_
    """
    class Meta:
        model = models.Author
        fields = '__all__'
        

class SagaSerializer (serializers.HyperlinkedModelSerializer):
    """API Endpoint that serialize Saga

    Args:
        serializers (_type_): _description_
    """
    class Meta:
        model = models.Saga
        fields = '__all__'
        
class BookSerializer (serializers.HyperlinkedModelSerializer):
    """API Endpoint that serialize Book

    Args:
        serializers (_type_): _description_
    """
    class Meta:
        model = models.Book
        fields = '__all__'