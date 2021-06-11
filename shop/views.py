from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm


# http://127.0.0.1:8000/shop/fructs/
def product_list(request, category_slug=None):
    print('category_slug = ', category_slug)
    # category_slug = 'fructs'
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    print("product id = ", product.id )
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                  'cart_product_form': cart_product_form})

# def main_page(request):
#     return  render(request,
#                   'shop/main_page.html',
#                   )  

def main_page(request):
    return  render(request,
                  'shop/bootstrap.html',
                  )  

