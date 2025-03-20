from django.shortcuts import render

def home(request):
    return render(request, "store/home.html")  # Ensure this template exists
