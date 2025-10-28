from django.urls import path
from .views import (
    FilmeListView,
    FilmeDetailView,
    FilmeCreateView,
    FilmeUpdateView,
    FilmeDeleteView,
)

urlpatterns = [
    path('', FilmeListView.as_view(), name='filme_list'),
    path('<int:pk>/', FilmeDetailView.as_view(), name='filme_detail'),
    path('novo/', FilmeCreateView.as_view(), name='filme_create'),
    path('<int:pk>/editar/', FilmeUpdateView.as_view(), name='filme_update'),
    path('<int:pk>/excluir/', FilmeDeleteView.as_view(), name='filme_delete'),
]