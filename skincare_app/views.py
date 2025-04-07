from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CustomerRegistrationForm
from .forms import ProductRegistrationForm

def register_customer(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.skin_issues = ','.join(form.cleaned_data['skin_issues'])  # Convert list to comma-separated string
            customer.save()
            messages.success(request, 'Customer registered successfully!')
            return redirect('register_customer')  # Redirect to the same page to show the success message
    else:
        form = CustomerRegistrationForm()
    return render(request, 'customers/register_customer.html', {'form': form})

def register_product(request):
    if request.method == 'POST':
        form = ProductRegistrationForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.skin_issues = ','.join(form.cleaned_data['skin_issues'])  # Convert list to comma-separated string
            product.save()
            messages.success(request, 'Product registered successfully!')
            return redirect('register_product')  # Stay on the same page
    else:
        form = ProductRegistrationForm()
    return render(request, 'products/register_product.html', {'form': form})