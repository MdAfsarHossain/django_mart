from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from django.core.paginator import Paginator

# Create your views here.

def store(request, category_slug=None):
    
    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        products = Product.objects.filter(is_available=True, category=category)  # Category wise products
        
        page = request.GET.get('page')
        paginator = Paginator(products, 1)  # It will show 1 products per page
        # paged_product = paginator.get_page(1)
        paged_product = paginator.get_page(page)
    else:
        products = Product.objects.filter(is_available = True)  # All products
        paginator = Paginator(products, 2)  # It will show 2 products per page        
        page = request.GET.get('page')
        # paged_product = paginator.get_page(2)
        paged_product = paginator.get_page(page)
        
        # for i in paged_product:
            # print(i)
        # print(paged_product.has_next(), paged_product.has_previous(), paged_product.previous_page_number(), paged_product.next_page_number())
        
    categories = Category.objects.all()
    context = {'products': paged_product, 'categories': categories, }
    return render(request, 'store/store.html', context)
    
    # return render(request, 'store/store.html')

def product_detail(request, category_slug, product_slug):
    single_product = Product.objects.get(slug = product_slug, category__slug = category_slug)
    
    print(single_product)
    
    # return render(request, 'store/product_detail.html')
    return render(request, 'store/product_detail.html', {'product': single_product})


