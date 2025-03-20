from django.urls import path
from .views import add_to_cart, view_cart, remove_from_cart

urlpatterns = [
    path('cart/', view_cart, name='cart'),
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove/<int:cart_id>/', remove_from_cart, name='remove_from_cart'),
]
