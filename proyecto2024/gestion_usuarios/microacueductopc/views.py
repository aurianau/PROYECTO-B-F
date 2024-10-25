from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Vivienda
from .serializers import ViviendaSerializer
from rest_framework import generics

# CRUD usando APIView

# GET, POST
class ViviendaList(APIView):
    def get(self, request):
        # Obtener todas las viviendas
        viviendas = Vivienda.objects.all()
        serializer = ViviendaSerializer(viviendas, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Crear nueva vivienda
        serializer = ViviendaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ViviendaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vivienda.objects.all()
    serializer_class = ViviendaSerializer

# GET, PUT, DELETE
class ViviendaRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        try:
            return Vivienda.objects.get(pk=pk)
        except Vivienda.DoesNotExist:
            return None

    def get(self, request, pk):
        # Obtener una vivienda por ID
        vivienda = self.get_object(pk)
        if vivienda is None:
            return Response({"error": "Vivienda no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ViviendaSerializer(vivienda)
        return Response(serializer.data)

    def put(self, request, pk):
        # Actualizar una vivienda existente
        vivienda = self.get_object(pk)
        if vivienda is None:
            return Response({"error": "Vivienda no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ViviendaSerializer(vivienda, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Eliminar una vivienda
        vivienda = self.get_object(pk)
        if vivienda is None:
            return Response({"error": "Vivienda no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        vivienda.delete()
        return Response({"message": "Vivienda eliminada"}, status=status.HTTP_204_NO_CONTENT)
