from django.shortcuts import render

def index(request):
    context = {
        'judul':'Rdx11',
        'subjudul':'Django Tutorial',
        'banner':'img/thanos.gif',
    }
    return render(request,'index.html',context)