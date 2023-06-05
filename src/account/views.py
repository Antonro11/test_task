from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from account.forms import RegistrationForm
from app.models import ShopCard, Shop


class Registration(CreateView):
    template_name = "registration/registration.html"
    form_class = RegistrationForm
    success_url = reverse_lazy("app:index")

    def form_valid(self, form):

        user = form.save()
        login(self.request, user=user, backend="django.contrib.auth.backends.ModelBackend")

        shop_card_instance = ShopCard.objects.create(
            balance=20
        )
        user.shop_card = shop_card_instance
        user.index_shop = Shop.objects.get(pk=1)
        user.save()

        return HttpResponseRedirect(reverse_lazy("app:index"))


class Login(LoginView):
    template_name = "registration/login.html"
    next_page = reverse_lazy("app:index")
    success_url = reverse_lazy("app:index")

class Logout(LogoutView):
    next_page = reverse_lazy("account:login")