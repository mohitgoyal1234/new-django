from django.shortcuts import render

# Create your views here.
def Faqs(request):
    return render(request,'faqs.html')
