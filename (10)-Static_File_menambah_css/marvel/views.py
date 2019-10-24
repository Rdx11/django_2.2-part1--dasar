from django.shortcuts import render

#code

def index(request):
    context = {
        'judul':'Rdx11',
        'subjudul':'Welcome to marvel page',
        'banner':'marvel/img/captain.gif',
    }
    return render(request,'index.html',context)