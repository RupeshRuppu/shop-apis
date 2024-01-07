# Create your views here.
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .utils import get_failed_response, get_success_response
from .models import MasterProducts
from .serializers import MasterProductsSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def root(request):
    return Response(get_success_response("Server is up and running"))


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_all_products(request):
    try:
        products = MasterProducts.objects.all()
        serializer = MasterProductsSerializer(products, many=True)
        return Response(get_success_response(serializer.data))

    except Exception as ex:
        return Response(get_failed_response(ex.args[0]))
