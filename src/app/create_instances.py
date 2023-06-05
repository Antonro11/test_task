from app.models import Product, Shop


def create_instances():
    if len(Product.objects.all()) == 0:
        Product.objects.create(product_name="Hamburger", price=4, product_image="static/product_image/hamb.jpg",
                               shop="Burger-King")
        Product.objects.create(product_name="Sandwich-Hamburger", price=5,
                               product_image="static/product_image/Sandwich-hamb.jpg",
                               shop="Burger-King")

        Product.objects.create(product_name="Habmurger + Fries + Cola", price=8,
                               product_image="static/product_image/MEnu.webp",
                               shop="Burger-King")

        Product.objects.create(product_name="Big-Mac", price=8,
                               product_image="static/product_image/big-mac.jpg",
                               shop="Mc Donalds")

        Product.objects.create(product_name="Mac-Double", price=9,
                               product_image="static/product_image/mcdonalds-double-big-mac-1_1-3-product-tile-desktop.jpg",
                               shop="Mc Donalds")
        Product.objects.create(product_name="Mac Menu", price=10,
                               product_image="static/product_image/DC_202201_8950_EVM_M_2Cheeseburger_Coke_Glass_832x472_1-3-product-t_TLmrsVR.jpg",
                               shop="Mc Donalds")
        Product.objects.create(product_name="Classic Cheese", price=4,
                               product_image="static/product_image/pizza_chees.jpg",
                               shop="Pizza Shop")
        Product.objects.create(product_name="Margarita", price=5,
                               product_image="static/product_image/pizza_margarita.jpg",
                               shop="Pizza Shop")
        Product.objects.create(product_name="Peperoni", price=5,
                               product_image="static/product_image/pizza_peperoni.webp",
                               shop="Pizza Shop")

    if len(Shop.objects.all()) == 0:
        burger_king = Shop.objects.create(shop_name="Burger-King", logo="static/logo/310_burgerking.jpg")
        for i in Product.objects.filter(shop="Burger-King"):
            burger_king.products.add(i)
            burger_king.save()

        mc_donalds = Shop.objects.create(shop_name="Mc Donalds", logo="static/logo/McDonalds_Golden_Arches.svg.png")
        for i in Product.objects.filter(shop="Mc Donalds"):
            mc_donalds.products.add(i)
            mc_donalds.save()

        pizza_shop = Shop.objects.create(shop_name="Pizza Shop",
                                         logo="static/logo/pizza-shop-logo-design-template-label-of-vector-20998926.jpg")
        for i in Product.objects.filter(shop="Pizza Shop"):
            pizza_shop.products.add(i)
            pizza_shop.save()
