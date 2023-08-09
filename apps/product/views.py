from django.core.cache import cache
from django.http import HttpResponse
from openpyxl.workbook import Workbook
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.product.models import Product
from apps.product.serializers import ProductListSerializer


class ProductListView(APIView):
    serializer_class = ProductListSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        cached_products = cache.get('product_list')

        if cached_products is None:
            queryset = (
                Product.objects
                .select_related('category')
                .prefetch_related('tags')
            )
            serializer = self.serializer_class(queryset, many=True)
            cached_products = serializer.data
            cache.set('product_list', serializer.data, 10)
        else:
            # Deserialize the cached data to a list of dictionaries
            cached_products = cached_products

        return Response(cached_products)


class ExportProductsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = (
            Product.objects
            .select_related('category')
            .prefetch_related('tags')
        )

        wb = Workbook()
        ws = wb.active
        ws.append(["ID", "Name", "Description", "Category", "Price", "Created At"])

        for product in queryset:
            created_at_str = product.created_at.strftime('%Y-%m-%d %H:%M:%S')
            ws.append(
                [
                    product.id, product.name, product.description,
                    product.category.name if product.category else "",
                    product.price, created_at_str
                ]
            )

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=products.xlsx'
        wb.save(response)

        return response
