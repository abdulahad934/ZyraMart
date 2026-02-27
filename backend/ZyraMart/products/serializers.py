from rest_framework import serializers
from django.utils.text import slugify
from .models import *
from django.db import transaction




class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category

        fields = ['id', 'name', 'slug', 'parent', 'is_active', 'created_at']
        read_only_fields = ['id', 'created_at']


    
    def validate_name(self, value):

        if not value.strip():
            raise serializers.ValidationError("category name is requerd. ")
        
        return value
    
    def valdate_slug(self, value):
        if Category.objects.filter(slug = value).exists():
            raise serializers.ValidationError("slug already Exists.")
        return value
    


    def create(self, validate_data):
        if not validate_data.get('slug'):
            validate_data['slug'] = slugify(validate_data['name'])

        return super().create(validate_data)
    

class AddBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'slug', 'logo', 'is_active', 'created_at']
        read_only_fields = ['id', 'created_at']

    
    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Brand name is requerd")
        return value
        
    def validate_slug(self, value):
        if Brand.objects.filter(slug = value).exists():
            raise serializers.ValidationError("slug already exists.")
        return value
    
    
    
    def create(self, validated_data):
        if not validated_data.get('slug'):
            validated_data['slug'] = slugify(validated_data['name'])
        return super().create(validated_data)
    



class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        exclude = ['product']
        extra_kwargs ={
            'discount_price': {'required': False, 'allow_null': True},
            'stock': {'required': False},
        }
    

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("price must be greater then 0.")
        return value
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image']


class ProductSerializer(serializers.ModelSerializer):
    variants = ProductVariantSerializer(many=True)
    images = ProductImageSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = '__all__'

    
    def validate_slug(self, value):
        if Product.objects.filter(slug = value).exists():
            raise serializers.ValidationError("slug already exists.")
        return value
    
    transaction.atomic

    def create(self, validated_data):
        variants_data = validated_data.pop('variants')
        images_data = validated_data.pop('images')

        product = Product.objects.create(**validated_data)

        for variant_data in variants_data:
            if not variant_data.get('sku'):
                variant_data['sku'] = f"{product.slug} -{variant_data.get('unit')}"

            
            ProductVariant.objects.create(
                product = product
                **variant_data
            )

        for image_data in images_data:
            ProductImage.objects.create(
                product = product
                **image_data
            )
        return product
