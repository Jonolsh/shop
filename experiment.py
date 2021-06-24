


a = {'2': 10, 55:'1000'}

print(a[55])



def cart(request):
    cart = Cart(request)
    return {'cart': cart}