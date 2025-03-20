from django import forms
from products.models import Product, Category

class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.filter(name__in=["Electronics", "Fashion", "Books", "Toys", "Groceries"]),
        empty_label="Select a category"
    )

    class Meta:
        model = Product
        fields = ["name", "price", "category", "stock", "description", "image"]