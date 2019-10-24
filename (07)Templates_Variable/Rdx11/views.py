from django.shortcuts import render

def index(request):
	context = {
		'judul':'Rdx11',
		'penulis':'@fiejiee',
	}
	return render(request,'index.html', context)
