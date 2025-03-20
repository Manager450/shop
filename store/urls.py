from django.urls import path
from .views import home, profile, discounted_products
from accounts.views import signup, login_view

urlpatterns = [
    path("", home, name="home"),  # This ensures / loads the homepage
    path("profile/", profile, name="profile"),
    path("discounted-products/", discounted_products, name="discounted_products"),
]
