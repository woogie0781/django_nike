from django.contrib import admin
from .models import Profile, OrderItem, Order

admin.site.register(Profile)
admin.site.register(Order)
admin.site.register(OrderItem)
