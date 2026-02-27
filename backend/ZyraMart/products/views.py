from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *





@api_view(['POST'])

@permission_classes([IsAuthenticated])

def add_category(request):
    serializer = CategorySerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

        return Response({
            "success": True,
            "message": "Category created Successfully!",
            "data": serializer.data
        }, status= 200)
    
    return Response({
        "sussess": False,
        "message": "Category Failds",
        "errors": serializer.errors
    }, status= 400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])

def add_brand(request):
    serializer = AddBrandSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            "success": True,
            "message": "Brand Created Successfully",
            "data": serializer.data
        }, status=200)
    
    return Response({
        "success": False,
        "message": "Add Brand Faild",
        "errors": serializer.errors
    }, status=400)






class AddProductAPIView(APIView):
    @transaction.atomic

    def post(self, request):
        serializer = ProductSerializer(data= request.data)

        if serializer.is_valid():
            product = serializer.save()
            return Response({
                'success': True,
                'message': "Product Add SuccessFully!",
                "product_id": product.id
            }, status=200)
        
        return Response({
            "success": False,
            "message": "Faild Added Product",
            "Errors": serializer.errors
        }, status=400)



