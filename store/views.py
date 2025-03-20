from django.shortcuts import render

from .models import Product, Category, Testimonial

def home(request):
    featured_products = Product.objects.filter(is_featured=True)[:6]  # Assuming 'is_featured' field
    categories = Category.objects.all()
    testimonials = Testimonial.objects.all()[:3]  # Display only 3 testimonials

    return render(request, "store/home.html", {
        "featured_products": featured_products,
        "categories": categories,
        "testimonials": testimonials
    })

def discounted_products(request):
    discounted_items = Product.objects.filter(price__lte=100)  # Example: Filter products under $100
    return render(request, "store/discounted_products.html", {"discounted_items": discounted_items})

def profile(request):
    return render(request, "store/profile.html")