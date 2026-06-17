from rest_framework.generics import ListCreateAPIView
from .serializers import ProductSerializer,SelfSerializers
from product.models import Product
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class ListAPi(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class ProductDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Product, pk=pk)

    def get(self, request, pk):
        obj = self.get_object(pk)
        return Response(SelfSerializers(obj).data)

    def put(self, request, pk):
        serializer = SelfSerializers(
            self.get_object(pk), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, pk):
        serializer = SelfSerializers(
            self.get_object(pk),
            data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT)
