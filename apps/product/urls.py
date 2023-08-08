from django.urls import path

from apps.product import views

urlpatterns = [
    path("products/", views.ProductListView.as_view(), name="product_list"),
    path('products/export/', views.ExportProductsView.as_view(), name='export-products'),
]
