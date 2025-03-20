from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from orders.models import Order
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from products.models import Product
from .forms import ProductForm  
from django.contrib.auth import logout
from django.shortcuts import redirect

# Ensure only admins can access
def admin_required(user):
    return user.is_authenticated and user.is_staff

@login_required
@user_passes_test(admin_required)
def admin_dashboard(request):
    total_products = Product.objects.count()
    total_orders = Order.objects.count()
    return render(request, "custom_admin/dashboard.html", {
        "total_products": total_products,
        "total_orders": total_orders
    })

# Ensure only staff/admin users can access
def admin_required(user):
    return user.is_authenticated and user.is_staff

# Admin Dashboard
@login_required
@user_passes_test(admin_required)
def admin_dashboard(request):
    total_products = Product.objects.count()
    return render(request, "custom_admin/dashboard.html", {
        "total_products": total_products,
    })

# List all products
@login_required
@user_passes_test(admin_required)
def product_list(request):
    products = Product.objects.all()
    return render(request, "custom_admin/product_list.html", {"products": products})

# Add new product
@login_required
@user_passes_test(admin_required)
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm()
    return render(request, "custom_admin/add_product.html", {"form": form})

# Edit existing product
@login_required
@user_passes_test(admin_required)
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm(instance=product)
    return render(request, "custom_admin/edit_product.html", {"form": form})

# Delete product
@login_required
@user_passes_test(admin_required)
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect("product_list")


@login_required
@user_passes_test(admin_required)
def order_list(request):
    orders = Order.objects.all()
    filter_status = request.GET.get("status")

    if filter_status:
        orders = orders.filter(status=filter_status)

    return render(request, "custom_admin/order_list.html", {"orders": orders})

def logout_confirmation(request):
    return render(request, "custom_admin/logout_confirmation.html")

def custom_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")  # Redirect to homepage after logout
    return redirect("logout_confirmation")

