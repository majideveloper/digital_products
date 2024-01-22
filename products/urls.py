from .views import (ProductListView,ProductDetailView,CategoryListView,CategoryDetailView,
                    FileListView,FileDetailView)
from django.urls import path

urlpatterns=[
    path('products/',ProductListView.as_view(),name='products-list'),
    path('products/<int:pk>/',ProductDetailView.as_view(),name='product-detail'),

    path('products/<int:product_pk>/files/',FileListView.as_view(),name='file-list'),
    path('products/<int:product_pk>/files/<int:pk>/',FileDetailView.as_view(),name='file-detail'),

    path('category/',CategoryListView.as_view(),name='category-list'),
    path('category/<int:pk>/',CategoryDetailView.as_view(),name='category-detail'),



]