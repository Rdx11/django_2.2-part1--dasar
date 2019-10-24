from django.shortcuts import render

def index(request):
    context = {
        'judul':'Rdx11',
        'subjudul':'welcome to app page',
        'banner':'myapp/img/app.jpg',
    }
    return render(request,'index.html',context)