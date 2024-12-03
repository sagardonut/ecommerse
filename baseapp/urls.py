
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home , name="home"),
    path('shop',views.shop , name="shop"),
    path('success/<pk>',views.sucess , name="sucess"),
    path('cancel',views.cancel , name="cancel"),
    path('product/<slug:slug>/',views.product_desc , name="product"),
    path('ai/pickoutfit',views.aipick , name='aipick'),
    path('add/cart/<slug:slug>/',views.add_to_cart, name='add_to_cart'),
    path('remove/cart/<int:product_id>/',views.aipick, name='remove_from_cart'),
    path('checkout/createSession/<slug:slug>',views.CreateCheckoutSession, name='create-checkout-session'),
    path('checkout/<slug:slug>',views.checkout , name="checkout/product"),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)