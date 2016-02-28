from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from listService.serializers import UserSerializer, GroupSerializer, ListElementSerializer
from .models import ListElement
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoit that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class JSONResponse(HttpResponse):
    """
    HTTP Response which renders into JSON
    """
    def __init__(self, data, **kwargs):
        """

        :rtype: JSONResponse
        """
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class ListElementView(APIView):
    """
    API endpoint that allows list elements to be viewed or edited
    """
    def get(self, request, format=None):
        """
        :param request:
        :param format:
        :return: List of list items
        """
        list_items = [list_item for list_item in ListElement.objects.all()]
        return Response(list_items)


@csrf_exempt
def element_list(request):
    """
    List of all elements
    :param request:
    :return:
    """
    if request.method == 'GET':
        list_elements = ListElement.objects.all()
        serializer = ListElementSerializer(list_elements, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ListElementSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

