from django.shortcuts import render

# Create your views here.

def BDA(request):
    context={}
    return render(request, 'BDA_app/BDA.html', context)
