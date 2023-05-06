from apps.forms import ProductForm
from apps.models import Product, ProductImage, Category
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404


def index_view(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'products/product-list.html', context)


def detail_view(request, id):
    product = get_object_or_404(Product, id=id)
    # product = Product.objects.filter(id=id).first()
    author_product = Product.objects.filter(author=product.author)[0:5]
    context = {
        'product': product,
        'author_product': author_product
    }
    return render(request, 'products/product-detail.html', context)


@login_required
def add_product(request):
    category = Category.objects.all()
    data = request.POST
    if request.method == 'POST':
        form = ProductForm(data, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.save()
            for image in request.FILES.getlist('images'):
                ProductImage.objects.create(image=image, product=product)
        return redirect('/')
    context = {
        'category': category
    }
    return render(request, 'products/add_product.html', context)
