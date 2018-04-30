# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import archivo
from .serializers import archivoserializer

# Regresa todos los videos
class ListArchivo(APIView):
	def get(self, request):
		archivos = archivo.objects.all()
		archivo_json = archivoserializer(archivos, many=True)
		return Response(archivo_json.data)

	def post(self, request):
		archivo_json = archivoserializer(data=request.data) #UnMarshall
		if archivo_json.is_valid():
			archivo_json.save()
			return Response(archivo_json.data, status=201)
		return Response(archivo_json.errors, status=400)

# Regresa especificamente el video por el pk
class DetailArchivo(APIView):
	def get_object(self, pk):
		try:
			return archivo.objects.get(pk=pk)
		except archivo.DoesNotExist:
			raise Http404

	def get(self, request, pk):
		archivos = self.get_object(pk)
		archivo_json = archivoserializer(archivos)
		return Response(archivo_json.data)

	# Actualiza dependiendo el pk que se le mande por la URL example: http://localhost:8000/archivos/pk
	def put(self, request, pk):
		archivos = self.get_object(pk)
		archivo_json = archivoserializer(archivos, data=request.data)
		if archivo_json.is_valid():
			archivo_json.save()
			return Response(archivoserializer.archivo_json.data)
		return Response(archivo_json.errors, status=400)
			
	# Elimina dependiendo el pk que se le mande por la URL example: http://localhost:8000/archivos/pk	
	def delete(self, request, pk):
		archivos = self.get_object(pk)
		archivos.delete()
		return Response(status=204)
