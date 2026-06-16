from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Product, Category, Review


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = 'id name description price category reviews rating'.split()
        depth = 1

    def get_reviews(self, product):
        return product.reviews_list


class ProductValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=255)
    description = serializers.CharField(required=False)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    category = serializers.IntegerField()

    def validate_category(self, category_id):
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise ValidationError('Category does not exist!')
        return category_id


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(required=True)
    product = serializers.IntegerField()
    stars = serializers.IntegerField(min_value=1, max_value=5)

    def validate_product(self, product_id):
        try:
            Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise ValidationError('Product does not exist!')
        return product_id