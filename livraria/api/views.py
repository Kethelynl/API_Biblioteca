from django.shortcuts import render
from rest_framework import generics
from .models import Livro
from .serializers import livroSerializers

class LivroListCreateView(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = livroSerializers

class LivroRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = livroSerializers