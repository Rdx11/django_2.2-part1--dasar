from django.shortcuts import render

# Create your views here.

def index(request):
	context = {
		'judul':'blog',
		'penulis':'Rdx11',
	}
	return render(request,'myapp/index.html',context)

def news(request):
	context = {
		'judul':'news',
		'penulis':'person1',
	}
	return render(request,'myapp/index.html',context)

def story(request):
	context = {
		'judul':'cerita',
		'penulis':'person2',
	}
	return render(request,'myapp/index.html',context)