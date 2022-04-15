from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_table),
    path('<int:pk>/', views.product_detail)
]    