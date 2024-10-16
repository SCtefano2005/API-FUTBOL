from django.urls import path
from .views import *

urlpatterns = [
    path('api/departamentos/', DepartamentoListView.as_view(), name='departamento-list'),
    path('api/departamentos/<int:departamento_id>/', DepartamentoDetailView.as_view(), name='departamento-detail'),
    path('', ClubListView.as_view(), name='club-list'),
    path('api/clubes/<int:club_id>/', ClubDetailView.as_view(), name='club-detail'),
]