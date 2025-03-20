from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic import RedirectView
from .views import (
    admin_dashboard, product_list, add_product, edit_product, delete_product, order_list, custom_logout
,logout_confirmation)

urlpatterns = [
    path("dashboard/", admin_dashboard, name="admin_dashboard"),
    path("products/", product_list, name="product_list"),
    path("products/add/", add_product, name="add_product"),
    path("products/edit/<int:product_id>/", edit_product, name="edit_product"),
    path("products/delete/<int:product_id>/", delete_product, name="delete_product"),
    path("orders/", order_list, name="order_list"),
    path("logout/", custom_logout, name="logout"),
    path("logout/confirm/", logout_confirmation, name="logout_confirmation"),
]
