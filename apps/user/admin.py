from django.contrib import admin
from .models import CustomUser
from .user_models.user_cart import UserCart
from .user_models.cart_products import CartProducts


# Register your models here.
admin.site.register(CustomUser)
admin.site.register(UserCart)
admin.site.register(CartProducts)

