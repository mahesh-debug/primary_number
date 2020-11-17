from django.urls import path
from .views import PrimeNumberChecker

urlpatterns = [
    # path("", views.homePage, "home"),
    path('get-prime-number/<slug:input_number>', PrimeNumberChecker.get_highest_prime_number_lower_than_input,
         name='get-prime-number'),

]
