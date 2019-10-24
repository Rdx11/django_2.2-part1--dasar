from django.http import HttpResponse

#method
def index(request):
    return HttpResponse("<h1>welcome to home pages</h1>")

def about(request):
	return HttpResponse("<h1> it is About Page </h1>")
