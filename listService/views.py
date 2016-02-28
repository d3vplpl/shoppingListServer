from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from listService.serializers import ListElementSerializer
from .models import ListElement
# Create your views here.


@api_view(['GET', 'POST'])
def element_list(request):
    """
    List of all elements
    :param request:
    :return:
    """
    if request.method == 'GET':
        list_elements = ListElement.objects.all()
        serializer = ListElementSerializer(list_elements, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ListElementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

