from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from coupons.forms import CouponApplyForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    print(request.COOKIES)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


# def cart_detail(request):
#     cart = Cart(request)
#     return render(request, 'cart/cart.html', {'cart': cart})
#     # return render(request, 'cart/detail.html', {'cart': cart})


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
                            initial={'quantity': item['quantity'],
                            'update': True})
    coupon_apply_form = CouponApplyForm()
    return render(request,
                  'cart/detail.html',
                  {'cart': cart,
                   'coupon_apply_form': coupon_apply_form})

#-------------------------------------------------------------------------

from django.shortcuts import render, HttpResponse
def test_session(request):
    print('*'*10)
    print(request.session.session_key)


    for key, value in request.session.items():
        print('{} => {}'.format(key, value))
    # после второго запроса во время действия сессии выведет:
    # test_session => {'session1': 'session1_test_data'}
    
    print('COOKIES')
    print(request.COOKIES)
    # сначала выведет  {}
    # а потом после второго запроса во время сессии выведет 
    # {'sessionid': 'ac0grqysir9dp8821boa4nmff4wp6p3h'}
    # т.е. в куках он хранти только sessionid пока


    session = request.session
    session['test_session'] = {'session1123':'session1_test_data'}

    if request.session.get('test', False):
        print('Test')
    else:
        session = request.session
        session['test_session'] = {'session1':'session1_test_data'}


    # print 
    return HttpResponse("Вы уже отправили комментарий11")





