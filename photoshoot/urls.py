from django.urls import path
from . import views
from .models import Gallery2018_19
from .models import Gallery2017_18
from .models import Gallery2016_17
from .models import Gallery2015_16


urlpatterns = [
    path('',views.photos)
]
