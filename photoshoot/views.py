from django.shortcuts import render

def photos(request):
    return render(request,'index.html')
