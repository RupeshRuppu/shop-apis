from django.urls import path
from .views import *


urlpatterns = [
    path("", root),
    path("get-products", get_all_products),
    path("get-filtered-products", filter_products),
]
