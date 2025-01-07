from django.urls import path
from .views import LivroListCreateView, LivroRetrieveUpdateDestroyView
app_name = 'api'  

urlpatterns = [
    path('livros/', LivroListCreateView.as_view(), name='livro-list-create'),
    path('livros/<int:pk>/', LivroRetrieveUpdateDestroyView.as_view(), name='livro-detail'),
]