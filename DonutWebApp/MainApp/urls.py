from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexPageView, name='index'),
    path('type/<str:typeName>', views.indexPageView, name='type'),
    path('big-donut', views.threeDimensionalDonutPageView, name='3d-donut'),
]