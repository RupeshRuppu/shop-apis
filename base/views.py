# Create your views here.
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .utils import get_failed_response, get_success_response
from .models import MasterProducts
from .serializers import MasterProductsSerializer
from django.shortcuts import render
from django.db.models import Q
import sys


@api_view(["GET"])
def root(request):
    return render(request, "index.html", {"data": "Server is up and running..."})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_all_products(request):
    try:
        products = MasterProducts.objects.all()
        serializer = MasterProductsSerializer(products, many=True)
        return Response(get_success_response(serializer.data))

    except Exception as ex:
        return Response(get_failed_response(ex.args[0]))


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def filter_products(request):
    """
    title, price(float), rating(float), size(int), category(single value or array of values), gender(a single value or ('M','F', 'C'))
    """

    # number value keys,
    _num_type_keys = set(["price", "rating", "size"])
    _list_type_keys = set(["category", "gender"])

    def get_value(key):
        nonlocal _body
        value = _body.get(key)
        if key in _list_type_keys:
            return value if isinstance(value, list) else [value]

        if key in _num_type_keys:
            return float(value) if isinstance(value, str) else value

        return value

    _body = request.data

    try:
        filters = {key: y for key in _body if (y := get_value(key)) is not None}
        products = MasterProducts.objects.filter(
            Q(title__icontains=filters.get("title", ""))
            | Q(category__in=filters.get("category", []))
            | Q(gender__in=filters.get("gender", []))
            | Q(price__lte=filters.get("price", sys.maxsize))
            | Q(rating__lte=filters.get("rating", sys.maxsize))
            | Q(size__lte=filters.get("size", sys.maxsize))
        )
        serializer = MasterProductsSerializer(products, many=True)
        return Response(get_success_response(serializer.data))

    except Exception as ex:
        return Response(get_failed_response(ex.args[0]))
