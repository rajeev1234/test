from django.contrib import admin
from .models import Todo,Cart,CartItem

class TodoAdmin(admin.ModelAdmin):
  list_display = ('title', 'rating', 'completed')
  search_fields = ['title',]

# Register your models here.
admin.site.register(Todo, TodoAdmin)


class CartAdmin(admin.ModelAdmin):
  search_fields = ['user',]
# Register your models here.
admin.site.register(Cart, CartAdmin)

class CartItemAdmin(admin.ModelAdmin):
  search_fields = ['price_ht',]


# Register your models here.
admin.site.register(CartItem, CartItemAdmin)