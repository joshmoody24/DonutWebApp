from django.shortcuts import render
from .models import *

# Create your views here.
def indexPageView(request, typeName="all"):
    if(typeName == "all"):
        donuts = Donut.objects.all()
    else:
        donuts = Donut.objects.filter(type__name=typeName)
    types = DonutType.objects.all()
    context ={
        'donuts': donuts,
        'donutTypes': types,
        'selectedType': typeName,
    }
    return render(request, "index.html", context)

def threeDimensionalDonutPageView(request):
    return render(request, "big_donut.html")