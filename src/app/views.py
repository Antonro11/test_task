import json

from django.shortcuts import render

from account.models import Account
from app.models import Shop, Product


# Create your views here.


def index(request):
    all_shops = Shop.objects.all()
    all_products = Product.objects.all()



    if request.method == "POST":
        data = json.loads(request.body)
        if "shop_pk" in data.keys():
            shop = Shop.objects.get(pk=data["shop_pk"])
            request.user.index_shop = shop
            request.user.save()

        elif "product_pk" in data.keys():
            product = Product.objects.get(pk=data["product_pk"])
            shop_card = request.user.shop_card
            shop_card.products = shop_card.products[:-1]+',{"product_name"'+':"'+product.product_name+'","price"'+':"'+str(product.price)+'"}]'
            if shop_card.products[0] == "[" and shop_card.products[1] == ",":
                shop_card.products = shop_card.products[0] + shop_card.products[2:]
            shop_card.save()

    if str(request.user) != 'AnonymousUser':
        card_balance = request.user.shop_card.balance
        json_card_products = json.loads(request.user.shop_card.products)

        return render(request, "index.html",
                      {"account": request.user, "all_shops": all_shops, "all_products": all_products,
                       "card_products": json_card_products, "card_balance": card_balance})

    return render(request, "index.html",
                  {"account": request.user, "all_shops": all_shops, "all_products": all_products, "admin_account": Account.objects.get(pk=1)})



def shop_card(request):
    card = request.user.shop_card
    card_balance = request.user.shop_card.balance
    json_card_products = json.loads(request.user.shop_card.products)
    total_bill = 0


    for i in json_card_products:
        total_bill += int(i["price"])

    bill_subtraction = total_bill-int(card_balance)

    if request.method == "POST":
        data = json.loads(request.body)
        if "delete" in data.keys():
            index_delete = int(data["delete"]) - 1
            card_user = request.user.shop_card
            products_on_card = json.loads(card_user.products)
            products_on_card.pop(index_delete)
            card_user.products = json.dumps(products_on_card)
            card_user.save()

        elif "pay" in data.keys():

            paying = int(card_balance) - total_bill
            if paying >= 0:
                card.balance = paying
                card.products = "[]"
                card.save()

    return render(request, "shop_card.html", {"card": card, "card_products": json_card_products, "card_balance": card_balance, "total_bill": total_bill, "bill_subtraction": bill_subtraction})



