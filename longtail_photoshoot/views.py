import os
from django.apps import apps
from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return HttpResponse('homepage')
    fy = request.GET.get('fy', '2018_19');
    tr = os.path.dirname(apps.get_app_config('photoshoot').path)
    #APP_ROOT = os.path.abspath(appname.__path__[0])
    #static_path = os.path.join(APP_ROOT, "some_file.txt")
    #path="C:\\somedirectory"  # insert the path to your directory
    path = tr + "\\static\\uploads\\" + fy
    ignored = {"thumb"}
    img_list = [x for x in os.listdir(path) if x not in ignored]
    fys = {"2015_16","2016_17","2017_18","2018_19"}
    return render(request,'index.html', {'images': img_list,'fy': fy,'fys': fys})
    #return render(request,'index.html')

def test(request):
    return render(request,'poshan.html')
