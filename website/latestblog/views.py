from django.shortcuts import render

# Create your views here.
def latestblog(request):
    return render(request,'latestblog.html')
