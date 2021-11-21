from rest_framework import routers
from product.api.viewsets import ProductViewset, ProductVariantViewset, ProductImageViewset

router = routers.DefaultRouter()

router.register(r'product', ProductViewset)
