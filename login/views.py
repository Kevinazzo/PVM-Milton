from django.shortcuts import render
from django.http import HttpResponse
import django.shortcuts
from pvm.wsgi import db

# Create your views here.

def login(request, usuario, password):
	if db.execute("SELECT * FROM Pvm_administrador WHERE nombre = '"+usuario+"' AND password = '"+password+"';" ).rowcount == 1:
		return HttpResponse(render("<h1> Correcto </h1>"))
	else:
		HttpResponse(render("<h1> NO EXISTE </h1>"))

def hola(request,id):
	result = db.execute("SELECT from Pvm_administrador WHERE id=" +id+";").fetchone()
	return HttpResponse(render(result[0]))