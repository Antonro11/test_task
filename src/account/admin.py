from django.contrib import admin


from account.models import Account
from app.models import Shop, Product, ShopCard, ShopIndexAnon


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Account)
admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(ShopCard)
admin.site.register(ShopIndexAnon)

