from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes, APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *


class AddCategoryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AddCategorySerializer(data = request.data)

        if serializer.is_valid:
            serializer.save()

            return Response({
                "success": True,
                "message": " Add Product successfully!",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            "success": False,
            "message": "Add Product Faild!",
            "errors": serializer.errors
        }, status=status.HTTP_401_UNAUTHORIZED)
    
# AddBrand Api 

class AddBrandAPIVew(APIView):

    def post(self, request):
        permission_classes = [IsAuthenticated]

        serializer = AddBrandSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({
                "success": True,
                "message": "Add Brand Successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            "success": False,
            "message": "Faild Brand added !",
            "errors": serializer.errors
        }, status=status.HTTP_401_UNAUTHORIZED)


# AddProduct Api

class AddProductAPIViw(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ProductImageSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({
                "success": True,
                "message": "Add Product successfully!",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "success": False,
            "message": "Faild Add Product",
            "errors": serializer.errors
        }, status=status.HTTP_401_UNAUTHORIZED)
    




