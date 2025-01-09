from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Livro
from .serializers import livroSerializers

class LivroListCreateView(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = livroSerializers
    permission_classes = [permissions.IsAuthenticated] #exige autenticação

class LivroRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = livroSerializers
    permission_classes = [permissions.IsAuthenticated]