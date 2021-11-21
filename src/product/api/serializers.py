from abc import ABC

from rest_framework import serializers

from product.models import Product, Variant, ProductVariant, ProductVariantPrice, ProductImage


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = '__all__'


class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = '__all__'


class ProductVariantPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariantPrice
        fields = '__all__'


class ProductImageSerializer(serializers.Serializer, ABC):
    class Meta:
        model = ProductImage
        fields = '__all__'
