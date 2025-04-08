from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CustomerRegistrationForm
from .forms import ProductRegistrationForm
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Customer, Product, Checkout, CheckoutProduct
from django.contrib import messages
from .models import Customer
from .models import Product
from .models import Checkout, CheckoutProduct
from .forms import RecommendProductsForm

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

def recommend_products(request):
    if request.method == 'POST':
        form = RecommendProductsForm(request.POST)

        if form.is_valid():
            customer_id = form.cleaned_data['customer_id']

            try:
                # Fetch the customer by ID
                customer = get_object_or_404(Customer, customer_id=customer_id)
            except Exception as e:
                print(f"Error fetching customer: {e}")
                messages.error(request, "Customer not found.")
                return render(request, 'recommendations/recommend_products.html', {'form': form})

            skin_type = customer.skin_type
            skin_issues = customer.skin_issues.split(',') if customer.skin_issues else []

            # Fetch products matching the customer's skin type and skin issues
            products = Product.objects.filter(skin_type=skin_type).filter(
                skin_issues__in=skin_issues
            ).distinct()

            # Render the template with customer and product data
            return render(request, 'recommendations/recommend_products.html', {
                'form': form,
                'customer': customer,
                'products': products,
                'customer_id': customer_id
            })
        else:
            # If the form is invalid, re-render the page with errors
            messages.error(request, "Please correct the errors below.")
            return render(request, 'recommendations/recommend_products.html', {'form': form})

    # Handle GET request (initial page load)
    form = RecommendProductsForm()
    return render(request, 'recommendations/recommend_products.html', {'form': form})

def checkout(request):
    if request.method == 'POST':
        print(request.POST)
        customer_id = request.POST.get('customer_id')
        customer_name = request.POST.get('customer_name')
        skin_type = request.POST.get('skin_type')
        skin_issues = request.POST.get('skin_issues')
        selected_products = request.POST.getlist('selected_products')
        product_prices = request.POST.getlist('product_prices')

        # Validate customer_id
        if not customer_id:
            messages.error(request, "Customer ID is required.")
            return redirect('recommend_products')

        # Validate selected products
        if not selected_products or not product_prices:
            messages.error(request, "No products selected.")
            return redirect('recommend_products')

        try:
            # Calculate total price
            total_price = sum(float(price) for price in product_prices)
        except ValueError:
            messages.error(request, "Invalid product prices.")
            return redirect('recommend_products')

        # Save checkout data
        checkout = Checkout.objects.create(
            customer_id=customer_id,
            customer_name=customer_name,
            skin_type=skin_type,
            skin_issues=skin_issues,
            total_price=total_price,
            payment_verified=True
        )

        # Save selected products
        for product_name, product_price in zip(selected_products, product_prices):
            CheckoutProduct.objects.create(
                checkout=checkout,
                product_name=product_name,
                product_price=product_price
            )

        # Add a success message
        messages.success(request, f"Payment verified for {customer_name} (ID: {customer_id}). Total: ${total_price:.2f}")

        # Redirect back to the recommendation page
        return redirect('recommend_products')

    return render(request, 'recommendations/recommend_products.html')

def list_customers(request):
    customers = Customer.objects.all()  # Fetch all customers from the database
    return render(request, 'customers/list_customers.html', {'customers': customers})

def list_products(request):
    products = Product.objects.all()  # Fetch all products from the database
    return render(request, 'products/list_products.html', {'products': products})

def list_checkouts(request):
    checkouts = Checkout.objects.all()  # Fetch all checkout records
    return render(request, 'checkouts/list_checkouts.html', {'checkouts': checkouts})