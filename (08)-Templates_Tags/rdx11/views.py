from django.shortcuts import render

def index(request):
	context = {
		'judul':'Rdx11',
		'subjudul':'Selamat datang',
		'nav': [
			['/','Home'],
			['/myapp','App'],
		]
	}
	return render(request,'index.html',context)





	