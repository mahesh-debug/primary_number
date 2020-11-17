from django.shortcuts import render
from django.http import JsonResponse
import math


# homepage
def homePage(request):
    return render(request, "highest_prime_number.html")


""" all prime numbers are greater than 1,
    prime number should be positive integers
    and NO prime numbers lower than 2 """


class PrimeNumberChecker:
    # when given input is prime number return True else False
    @staticmethod
    def is_prime_number(user_input):
        if user_input <= 1:
            return False
        if user_input == 2:
            return True
        if user_input > 2 and user_input % 2 == 0:
            return False
        max_div = math.floor(math.sqrt(user_input))
        for i in range(3, 1 + max_div, 2):
            if user_input % i == 0:
                return False
        return True

    # get last prime number lower than input number
    @staticmethod
    def get_highest_prime_number_lower_than_input(request, input_number):
        _prime_number = 0
        _no_of_prime_num = 0
        input_number = int(input_number)
        if int(input_number) > 2:
            if _no_of_prime_num < 1:
                for _number in reversed(range(1, input_number)):
                    if PrimeNumberChecker.is_prime_number(_number):
                        _prime_number = _number
                        _no_of_prime_num = 1
                        if _prime_number:
                            break

            if _prime_number:
                context = {
                    "response": f"Highest prime number lower than {input_number}: {_prime_number}"
                }

                return JsonResponse(context)
            else:
                context = {
                    "response":
                        f"No prime number found. please check your input{_prime_number}",

                }
                return JsonResponse(context)
        elif int(input_number) <= 1:
            context = {
                "response": f"{input_number} is NOT a Natural Number, A Prime Number must be greater than 1"
            }
            return JsonResponse(context)
        elif int(input_number) == 2:
            context = {
                "response": f"NO Prime number found lower than {input_number}"
            }
            return JsonResponse(context)
