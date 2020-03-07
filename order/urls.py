
from django.urls import path
from . import views

app_name = "order"

urlpatterns = [
    path('to-checkout/', views.ToCheckout.as_view(), name='to-checkout'),
    # path('complete/', views.CompleteView.as_view(), name='complete'),
    path('complete/<int:order_no>/', views.CompleteView.as_view(), name='complete'),
    path('make-order/', views.MakeOrder.as_view(), name='make-order'),
    path('checkout/', views.checkout, name='checkout'),
    path('shipping/', views.Shippings, name='shipping'),
    path('shipping-show/', views.ShippingShow, name='shipping-show'),
]
