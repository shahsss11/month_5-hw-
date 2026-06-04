from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Category, Review
from .serializers import ProductSerializer, CategorySerializer, ReviewSerializer
from django.db import transaction   

@api_view(['GET', "POST"])
def product_list_create_api_view(request):
    if request.method == 'POST':
        name = request.data.get('name')
        description = request.data.get('description')
        price = request.data.get('price')
        category_id = request.data.get('category')
        with transaction.atomic():
            product = Product.objects.create(
                name=name,
                description=description,
                price=price,
                category_id=category_id
            )
            product.save()
            return Response(
                status=status.HTTP_201_CREATED,
                data=ProductSerializer(product, many=False).data
            )
    elif request.method == 'GET':
        Products = Product.objects.all()
        list_ = ProductSerializer(Products, many=True).data
        return Response(
            data=list_
        )

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_create_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
            return Response(
                data={'error': 'Product not found'},
                status=status.HTTP_404_NOT_FOUND
            )
    if request.method == 'GET':
        data = ProductSerializer(product, many=False).data
        return Response(
            data=data)
    elif request.method == 'PUT':
        product.name = request.data.get('name')
        product.description = request.data.get('description')
        product.price = request.data.get('price')
        product.category_id = request.data.get('category')
        product.save()
        return Response(
            data=ProductSerializer(product, many=False).data)
    elif request.method == 'DELETE':
        product.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT)
    
    data = ProductSerializer(product, many=False).data
    return Response(
        data=data)

@api_view(['GET', 'POST'])
def category_list_create_api_view(request):
    if request.method == "GET":
        category = Category.objects.all()
        list = CategorySerializer(category, many=True).data
        return Response(
            data=list)
    elif request.method == "POST":
        name = request.data.get('name')
        with transaction.atomic():
            category = Category.objects.create(
                name=name
            )
            category.save()
            return Response(
                status=status.HTTP_201_CREATED,
                data=CategorySerializer(category, many=False).data
            )


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail_create_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(
            data={'error': 'Category not found'},
            status=status.HTTP_404_NOT_FOUND
        )
    if request.method == 'GET':
        data = CategorySerializer(category, many=False).data
        return Response(
            data=data)
    elif request.method == 'PUT':
        category.name = request.data.get('name')
        category.save()
        return Response(
            data=CategorySerializer(category, many=False).data)
    elif request.method == 'DELETE':
        category.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT)
    
    data = CategorySerializer(category, many=False).data
    return Response(
        data=data)

@api_view(['GET', 'POST'])
def review_list_create_api_view(request):
    if request.method == "POST":
        text = request.data.get('text')
        product_id = request.data.get('product')
        stars = request.data.get('stars')
        with transaction.atomic():
            review = Review.objects.create(
                text=text,
                product_id=product_id,
                stars=stars
            )
            review.save()
            return Response(
                status=status.HTTP_201_CREATED,
                data=ReviewSerializer(review, many=False).data
            )
    elif request.method == "GET":
        review = Review.objects.all()
        list = ReviewSerializer(review, many=True).data
        return Response(
            data=list)

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_create_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(
            data={'error': 'Review not found'},
            status=status.HTTP_404_NOT_FOUND
        )
    if request.method == 'GET':
        data = ReviewSerializer(review, many=False).data
        return Response(
            data=data)
    elif request.method == 'PUT':
        review.text = request.data.get('text')
        review.product_id = request.data.get('product')
        review.stars = request.data.get('stars')
        review.save()
        return Response(
            data=ReviewSerializer(review, many=False).data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT)

    data = ReviewSerializer(review, many=False).data
    return Response(
        data=data)

@api_view(['GET'])
def products_reviews(request):
    products = Product.objects.all()
    list_ = ProductSerializer(products, many=True).data
    return Response(
        data=list_
    )
