from rest_framework import viewsets
from product.models import Product, Variant, ProductVariant, ProductImage

from .serializers import ProductSerializer, ProductVariantSerializer


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductVariantViewset(viewsets.ModelViewSet):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer


# class ProductImageViewset(viewsets.ModelViewSet):
#     queryset = ProductImage.objects.all()
#     serializer_class = ProductImageSerializer
