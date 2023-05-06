from apps.forms import ProductForm
from apps.models import Product, ProductImage, Category
from django.contrib.auth.decorators import login_required

@login_required(login_url='users/login')
def index_view(request):
    products = Product.objects.all()
    return render(request,'index.html',context={"products": products})


from django.shortcuts import render, redirect


def detail_view(request,id):
    product = Product.objects.filter(id=str(id)).first()
    author_product = Product.objects.filter(author=product.author)[0:5]
    context = {
        'product': product,
        'author_product': author_product
    }
    return render(request,'product.html',context)


@login_required
def add_product(request):
    category = Category.objects.all()
    data = request.POST
    if request.method == 'POST':
        form = ProductForm(data,request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.save()
            for image in request.FILES.getlist('images'):
                ProductImage.objects.create(image=image, product=product)
        return redirect('/')
    return render(request, 'add_product.html', {'category': category})



