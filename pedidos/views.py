from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def consultaUsuario(request, id):
	return HttpResponse('<h1>'+id+'</h1>')