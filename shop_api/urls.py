from django.contrib import admin
from django.urls import path
from Product import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/products/', views.product_list),
    path('api/v1/products/<int:id>/', views.product_detail),
    path('api/v1/categories/', views.category_list),
    path('api/v1/categories/<int:id>/', views.category_detail),
    path('api/v1/reviews/', views.review_list),
    path('api/v1/reviews/<int:id>/', views.review_detail),
    path('api/v1/products/reviews/', views.products_reviews)
]
