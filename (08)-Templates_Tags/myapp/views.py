from django.shortcuts import render

# Create your views here.

def index(request):
	context = {
		'judul':'Rdx11',
		'subjudul':'Myapp',
		'nav': [
			['/','Home'],
		]
	}
	return render(request,'index.html',context)