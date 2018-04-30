from rest_framework import serializers
from .models import archivo
from django.contrib.auth.models import User

class usuarioserializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id','username','email')

class archivoserializer(serializers.ModelSerializer):
	autor = usuarioserializer(read_only=True)
	class Meta:
		model = archivo
		fields = ('id', 'nombre_archivo', 'archivo', 'autor')