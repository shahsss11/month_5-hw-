from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Category, Review
from .serializers import ProductSerializer, CategorySerializer, ReviewSerializer

@api_view(['GET'])
def product_list(request):
    product = Product.objects.all()
    list = ProductSerializer(product, many=True).data
    return Response(
        data=list)

@api_view(['GET'])
def product_detail(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(
            data={'error': 'Product not found'},
            status=status.HTTP_404_NOT_FOUND
        )
    data = ProductSerializer(product, many=False).data
    return Response(
        data=data)

@api_view(['GET'])
def category_list(request):
    category = Category.objects.all()
    list = CategorySerializer(category, many=True).data
    return Response(
        data=list)

@api_view(['GET'])
def category_detail(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(
            data={'error': 'Category not found'},
            status=status.HTTP_404_NOT_FOUND
        )
    data = CategorySerializer(category, many=False).data
    return Response(
        data=data)

@api_view(['GET'])
def review_list(request):
    review = Review.objects.all()
    list = ReviewSerializer(review, many=True).data
    return Response(
        data=list)

@api_view(['GET'])
def review_detail(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(
            data={'error': 'Review not found'},
            status=status.HTTP_404_NOT_FOUND
        )
    data = ReviewSerializer(review, many=False).data
    return Response(
        data=data)
