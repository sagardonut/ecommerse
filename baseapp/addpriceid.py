from .models import products
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRETKEY

for product in products.objects.all():
    passR