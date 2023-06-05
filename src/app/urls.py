from django.urls import path

from app.views import index, shop_card

app_name = "app"

urlpatterns = [
    path('', index, name="index"),
    path('card', shop_card, name="card"),
    ]