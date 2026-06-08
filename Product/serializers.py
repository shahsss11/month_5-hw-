from rest_framework import serializers
from .models import Product, Category, Review

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'products_count']

class ProductSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'reviews', 'rating']
        
    def get_reviews(self, product):
        return product.reviews_list
    
    def get_rating(self, product):
        return product.rating

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text product stars'.split()

class ProductValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    category = serializers.IntegerField()
    def validate_category(self, category_id):
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise serializers.ValidationError('Category not found')
        return category_id

class CategoryValidateSerializer(ProductValidateSerializer):
    name = serializers.CharField(max_length=255) 


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    product = serializers.IntegerField()
    stars = serializers.IntegerField(min_value=1, max_value=5)
    def validate_product(self, product_id):
        try:
            Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise serializers.ValidationError('Product not found')
        return product_id
