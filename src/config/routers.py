from rest_framework import routers
from product.api.viewsets import ProductViewset, ProductVariantViewset

router = routers.DefaultRouter()

router.register(r'product', ProductViewset)
