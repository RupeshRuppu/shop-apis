from rest_framework.serializers import ModelSerializer
from .models import MasterProducts


class MasterProductsSerializer(ModelSerializer):
    class Meta:
        model = MasterProducts
        fields = "__all__"
