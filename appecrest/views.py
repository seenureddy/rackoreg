from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exmpert
from django.shortcuts import render
from django.contrib.auth.models import User, Group

from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParsers

from .models import Snippet
from .serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializers_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    qureyset = Group.objects.all()
    serializers_class = GroupSerializer

class JSONResponse(HttpResponse):
    """
    HttpResponse that render it's content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json' 
        super(JSONResponse, self).__init__(content, **kwargs)