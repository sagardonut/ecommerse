from django.shortcuts import render,HttpResponse,get_object_or_404,redirect,reverse
from django.contrib import messages
from django.http import JsonResponse
from django.conf import settings
from .models import products
import stripe

stripe.api_key = settings.STRIPE_SECRETKEY

# Create your views here.
def home(request):
    # request.session.flush()
    product = products.objects.all()
    cart = request.session.get('cart', {})
    total_price = 0
    for item in cart.values():
        total_price += float(item['bill_amt']) * item['quantity']
        
    return render(request,"index.html",
                  {
                      "products":product,
                      "cart":cart, 
                      'bill_amt':total_price,
                      
                   })

def aipick(request):
    product = products.objects.all()
    if request.method == "POST":
        pass
    return render(request,"ai.html",{"products":product})
    

def product_desc(request,slug):
    product = get_object_or_404(products,slug=slug)
    stripe_pub_key= settings.STRIPE_PUBLICABLEKEY
    cart = request.session.get('cart', {})
    total_price = 0
    for item in cart.values():
        total_price += float(item['bill_amt']) * item['quantity']
    
    return render(request, 'frabic.html' ,
                  { "product":product,
                   "cart":cart, 
                   'bill_amt':total_price,
                   'stripe_pub_key':stripe_pub_key,
                   })

def add_to_cart(request, slug):
    product = products.objects.get(slug=slug)
    cart =request.session.get('cart',{})
    if str(product.slug) in cart:
        cart[str(product.slug)]["quantity"] += 1
    else:
        cart[str(product.slug)] = {
            "item":product.name,
            "bill_amt" : str(product.price),
            "quantity" : 1,
            "img_url" :product.img.url
        }
        messages.success(request,"Item added to cart ")
    request.session['cart'] = cart
    return redirect('home')

def CreateCheckoutSession(request, slug):
    product = products.objects.get(slug=slug)
    YOUR_DOMAIN = "https:/127.0.0.1:8000"
    if request.method == "POST":
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': "price_1QRsgnLcmnchVaXZriiFMYbE",
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='http://127.0.0.1:8000/success/'+ f'{product.id}',
            cancel_url='http://127.0.0.1:8000/cancel'
        )
    return JsonResponse({ 'id':checkout_session.id })

def checkout(request,slug):
    product = products.objects.get(slug=slug)
    return render(request, 'checkout.html', { "product":product})

def shop(request):
    return redirect("home")

def sucess(request,pk):
    product= products.objects.get(id=pk)
    return render(request,'sucess.html',{"product":product})

def cancel(request):
    return render(request,'cancel.html')