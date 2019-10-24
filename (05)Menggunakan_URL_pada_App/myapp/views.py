from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request,'myapp.html')

def hello(request):
	return HttpResponse('<h1> hello world </h1>')