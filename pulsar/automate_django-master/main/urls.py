from django.urls import path, include
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from main import views
from .models import Device
from .views import DeviceListView

from django.conf.urls import url

from .views import SwitchListView
from .views import Switch2ListView
from .views import BoardListView
from .views import PruebaListView
from .views import PuzzleListView
from .views import Caro2ListView


urlpatterns = [
    path('', DeviceListView.as_view(), name="home"),
    path('switch/', SwitchListView.as_view(), name="Switch"),
    path('board/', BoardListView.as_view(), name="Board"),
    path('caro2/', Caro2ListView.as_view(), name="Galeria"),
    path('puzzle/', PuzzleListView.as_view(), name="Puzzle"),
    path('prueba/', PruebaListView.as_view(), name="Prueba"),    
    path('devices/', views.DeviceList.as_view(), name='device-list'),
    path('switch2/', Switch2ListView.as_view(), name="Switch2"),
    path('devices/<int:pk>/', views.DeviceDetail.as_view(), name='device-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail'),
    path('api/', views.api_root),
]
