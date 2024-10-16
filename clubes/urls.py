from django.urls import path
from .views import ClubListView, ClubDetailView, DepartamentoListView

urlpatterns = [
    path('api/departamentos/', DepartamentoListView.as_view(), name='departamento-list'),
    path('', ClubListView.as_view(), name='club-list'),
    path('api/clubes/<int:club_id>/', ClubDetailView.as_view(), name='club-detail'),
]