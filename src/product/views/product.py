from django.views import generic

from product.models import Variant, Product, ProductVariantPrice, ProductVariant


class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context


class ProductListView(generic.ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/list.html'
    paginate_by = 10

    def get_queryset(self):
        products = super().get_queryset()
        if self.request.GET.get('title'):
            title = self.request.GET.get('title')
            print(title)
            products = Product.objects.filter(title__icontains=title)
        if self.request.GET.get('variant'):
            variant = self.request.GET.get('variant')
            print(variant)
            # variant
            # products = products.filter()
        if self.request.GET.get('date'):
            date = self.request.GET.get('date')
            print(date)
            products = products.filter(created_at__gte=date)
        if self.request.GET.get('price_from', 'price_to'):
            price_from = self.request.GET.get('price_from', 0)
            print(price_from)
            price_to = self.request.GET.get('price_to', 9999999999)
            print(price_to)
            products = Product.objects.filter(productvariantprice__price__range=(price_from, price_to))
            return products

        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['variants'] = ProductVariant.objects.all()
        # product_variant_price = ProductVariantPrice.objects.first()
        # context['product_variant_price'] = product_variant_price
        return context
