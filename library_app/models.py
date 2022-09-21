from pyexpat import model
from tokenize import String
from turtle import title
from django.db import models

# Create your models here.


class Author (models.Model):
    """
    Entity that rappresent an Author
    """
    id = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    born_date = models.DateField('date_of_birth')

    def __str__(self) -> str:
        return f"{self.first_name} {self.second_name}"

class Saga (models.Model):
    """
    Entity that rappresent a group of book
    """
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name

class Book (models.Model):
    """
    Entity that rappresent a Book
    """
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    summary = models.TextField(max_length=5000)
    isSaga = models.BooleanField(default=False)
    saga = models.ForeignKey(Saga, on_delete=models.SET_NULL, null=True, blank=True)
    sagaSequence = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title
    