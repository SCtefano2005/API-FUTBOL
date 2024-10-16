from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Club, Departamento
from .serializers import ClubDetailSerializer, ClubCreateSerializer, DepartamentoSerializer

class DepartamentoListView(APIView):
    def get(self, request):
        departamentos = Departamento.objects.all()
        serializer = DepartamentoSerializer(departamentos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DepartamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DepartamentoDetailView(APIView):
    def get(self, request, departamento_id):
        try:
            departamento = Departamento.objects.get(pk=departamento_id)
        except Departamento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DepartamentoSerializer(departamento)
        return Response(serializer.data)

    def put(self, request, departamento_id):
        try:
            departamento = Departamento.objects.get(pk=departamento_id)
        except Departamento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DepartamentoSerializer(departamento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, departamento_id):
        try:
            departamento = Departamento.objects.get(pk=departamento_id)
        except Departamento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        departamento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ClubListView(APIView):
    def get(self, request):
        departamento = request.GET.get('departamento', None)
        nombre = request.GET.get('nombre', None)
        estadio = request.GET.get('estadio', None)
        fecha_fundacion_inicio = request.GET.get('fecha_fundacion_inicio', None)
        fecha_fundacion_fin = request.GET.get('fecha_fundacion_fin', None)

        clubes = Club.objects.all()

        if departamento:
            clubes = clubes.filter(departamento__nombre__icontains=departamento)  # Filtrar por nombre del departamento
        if nombre:
            clubes = clubes.filter(nombre__icontains=nombre)  # Filtrar por nombre del club
        if estadio:
            clubes = clubes.filter(estadio__icontains=estadio)  # Filtrar por nombre del estadio
        if fecha_fundacion_inicio:
            clubes = clubes.filter(fecha_fundacion__gte=fecha_fundacion_inicio)  # Filtrar por fecha de fundación desde
        if fecha_fundacion_fin:
            clubes = clubes.filter(fecha_fundacion__lte=fecha_fundacion_fin)  # Filtrar por fecha de fundación hasta

        serializer = ClubDetailSerializer(clubes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClubCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClubDetailView(APIView):
    def get(self, request, club_id):
        try:
            club = Club.objects.get(pk=club_id)
        except Club.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ClubDetailSerializer(club)
        return Response(serializer.data)

    def put(self, request, club_id):
        try:
            club = Club.objects.get(pk=club_id)
        except Club.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ClubCreateSerializer(club, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, club_id):
        try:
            club = Club.objects.get(pk=club_id)
        except Club.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        club.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)