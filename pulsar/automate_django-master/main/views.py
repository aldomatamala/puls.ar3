from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.views.generic.list import ListView

from .models import Device
from .permissions import IsOwnerOrReadOnly
from .serializers import DeviceSerializer, UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'devices': reverse('device-list', request=request, format=format)
    })


class DeviceListView(ListView):
    model = Device
    context_object_name = 'devices'
    # queryset = Device.objects.all()
    template_name = 'home.html'

    def get_queryset(self):
        if(self.request.user.is_authenticated):
            return Device.objects.filter(owner=self.request.user)

class SwitchListView(ListView):
    model = Device
    context_object_name = 'devices'
    # queryset = Device.objects.all()
    template_name = 'switch.html'

    def get_queryset(self):
        if(self.request.user.is_authenticated):
            return Device.objects.filter(owner=self.request.user)

class BoardListView(ListView):
    model = Device
    context_object_name = 'devices'
    # queryset = Device.objects.all()
    template_name = 'board.html'

    def get_queryset(self):
        if(self.request.user.is_authenticated):
            return Device.objects.filter(owner=self.request.user)

class PruebaListView(ListView):
    model = Device
    context_object_name = 'devices'
    # queryset = Device.objects.all()
    template_name = 'prueba.html'

    def get_queryset(self):
        if(self.request.user.is_authenticated):
            return Device.objects.filter(owner=self.request.user)

class PuzzleListView(ListView):
    model = Device
    context_object_name = 'devices'
    # queryset = Device.objects.all()
    template_name = 'puzzle.html'

    def get_queryset(self):
        if(self.request.user.is_authenticated):
            return Device.objects.filter(owner=self.request.user)

class DeviceList(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

class Switch2ListView(ListView):
    model = Device
    context_object_name = 'devices'
    # queryset = Device.objects.all()
    template_name = 'switch2.html'

    def get_queryset(self):
        if(self.request.user.is_authenticated):
            return Device.objects.filter(owner=self.request.user)
            
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class Caro2ListView(ListView):
    model = Device
    context_object_name = 'devices'
    # queryset = Device.objects.all()
    template_name = 'caro2.html'

    def get_queryset(self):
        if(self.request.user.is_authenticated):
            return Device.objects.filter(owner=self.request.user)    


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
