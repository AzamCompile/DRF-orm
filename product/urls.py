from django.urls import path
from .views import ListAPi,ProductDetailAPIView

urlpatterns = [
    path('',ListAPi.as_view(),name='ListAPi'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
]