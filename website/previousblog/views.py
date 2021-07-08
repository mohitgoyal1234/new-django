from django.shortcuts import render

# Create your views here.
def previousblog(request):
    return render(request,'previousblog.html')
