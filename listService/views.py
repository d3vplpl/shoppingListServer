from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from listService.serializers import ListElementSerializer, ShopListSerializer
from .models import ListElement, ShopList
# Create your views here.


@api_view(['GET', 'POST'])
def element_list(request, format=None):
    """
    List of all elements
    :param request:
    :return:
    """

    if request.method == 'GET':
        shop_lists = ShopList.objects.all()
        serializer_lists = ShopListSerializer(shop_lists, many=True)
        list_elements = ListElement.objects.all()
        serializer = ListElementSerializer(list_elements, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ListElementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', 'GET'])
def element_detail(request, pk):
    try:
        el_detail = ListElement.objects.get(pk=pk)
    except ListElement.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ListElementSerializer(el_detail)
        return Response(serializer.data)

    if request.method == 'DELETE':
        el_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'DELETE'])
def element_detail_by_name(request, item_name):
    try:
        el_detail = ListElement.objects.get(item_name=item_name)
    except ListElement.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ListElementSerializer(el_detail)
        return Response(serializer.data)
    if request.method == 'DELETE':
        el_detail.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
