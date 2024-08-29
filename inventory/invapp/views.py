from django.shortcuts import render ,redirect

# Create your views here.
from .forms import ProductForm
from .models import Product

def home_view(request):
    return render(request, 'invapp/home.html')


def product_create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'invapp/product_form.html', {'form':form})


def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'invapp/product_list.html',{'products':products})


def product_update_view(request, product_id):
    # Fetch the product object
    product = Product.objects.get(product_id=product_id)
    
    if request.method == 'POST':
        # Bind the form with POST data and the product instance
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        # Initialize the form with the product instance for a GET request
        form = ProductForm(instance=product)
    
    # Render the form template with the form object
    return render(request, 'invapp/product_form.html', {'form': form})



def product_delete_view(request,product_id):
    product = Product.objects.get(product_id = product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'invapp/product_conf_del.html', {'product':product})