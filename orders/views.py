from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.conf import settings
import stripe
from django.views.decorators.csrf import csrf_exempt
import json


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            
            # order = form.save()

            order = form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            order.save()


            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            return render(request, 'orders/order/created.html',
                          {'order': order, 'stripe_publishable_key':settings.STRIPE_PUBLISHABLE_KEY})
    else:
        form = OrderCreateForm
    # return render(request, 'orders/order/create.html',
    #               {'cart': cart, 'form': form})
    return render(request, 'orders/order/new_create_form.html',
                  {'cart': cart, 'form': form})



@csrf_exempt
def create_checkout_session(request, id):

    request_data = json.loads(request.body) # словарь
    # get_object_or_404 - получить объект если его нет вернет страницу ошибки
    product = get_object_or_404(Product, pk=id)

    stripe.api_key = settings.STRIPE_SECRET_KEY
    checkout_session = stripe.checkout.Session.create(
        # Customer Email is optional,
        # It is not safe to accept email directly from the client side
        customer_email = request_data['email'],
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                    'name': product.name,
                    },
                    'unit_amount': int(product.price * 100),
                },
                'quantity': 1,
            }
        ],
        mode='payment',
        success_url=request.build_absolute_uri(
            reverse('success')
        ) + "?session_id={CHECKOUT_SESSION_ID}",
        cancel_url=request.build_absolute_uri(reverse('failed')),
    )

    # OrderDetail.objects.create(
    #     customer_email=email,
    #     product=product, ......
    # )

    order = OrderDetail()
    order.customer_email = request_data['email']
    order.product = product
    order.stripe_payment_intent = checkout_session['payment_intent']
    order.amount = int(product.price * 100)
    order.save()

    # return JsonResponse({'data': checkout_session})
    return JsonResponse({'sessionId': checkout_session.id})