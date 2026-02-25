from rest_framework import serializers
from django.utils.text import slugify
from .models import Category



# class CategorySerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Category
#         fields = ['id', 'name', 'slug', 'parent', 'is_active', 'created_at']
#         read_only_fields = ['id', 'created_at']

#     def validate_name(self, value):
#         if not value.strip():
#             raise serializers.ValidationError("Category name is required.")
#         return value

#     def validate_slug(self, value):
#         if Category.objects.filter(slug=value).exists():
#             raise serializers.ValidationError("Slug already exists.")
#         return value

#     def create(self, validated_data):
#         if not validated_data.get('slug'):
#             validated_data['slug'] = slugify(validated_data['name'])
#         return super().create(validated_data)



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