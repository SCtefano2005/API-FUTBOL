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
        clubes = Club.objects.all()
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
