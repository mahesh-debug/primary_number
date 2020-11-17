from unittest import TestCase
from django.urls import resolve
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.keys import Keys

from stably.views import get_highest_prime_number, homePage
import time


# url testing
class TestUrls(TestCase):

    # homepage
    def test_url_for_homepage(self):
        resolver = resolve('/')
        self.assertEqual(resolver.func, homePage)

    # prime number
    def test_url_for_get_highest_prime_number(self):
        resolver = resolve('/stably/get-prime-number/1')
        self.assertEqual(resolver.func, get_highest_prime_number)


# functional test cases
class TestingGetPrimeNumber(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path="C:/Users/geckodriver")

    def tearDown(self):
        self.browser.close()

    # user request homepage the first time
    def test_open_get_prime_number_homepage(self):
        self.browser.get(self.live_server_url)
        time.sleep(1)

    # user input 1
    # give response 1 is NOT a Prime Number, A Prime Number must be greater than 1
    def test_when_user_enter_input_1(self):
        self.browser.get(self.live_server_url)
        alert = self.browser.find_element_by_id("input_number")
        alert.send_keys("1")
        alert.send_keys(Keys.TAB)
        time.sleep(1)
        self.assertEqual(
            self.browser.find_element_by_id("prime_number").text,
            "1 is NOT a Prime Number, A Prime Number must be greater than 1"
        )

    # user input 2
    # response NO Prime number found lower than 2
    def test_when_user_enter_input_2(self):
        self.browser.get(self.live_server_url)
        alert = self.browser.find_element_by_id("input_number")
        alert.send_keys("2")
        alert.send_keys(Keys.TAB)
        time.sleep(1)
        self.assertEqual(
            self.browser.find_element_by_id("prime_number").text,
            "NO Prime number found lower than 2"
        )

    # when user input valid number
    # response prime number should be lower than given input
    def test_when_user_enter_input_valid_number(self):
        self.browser.get(self.live_server_url)
        alert = self.browser.find_element_by_id("input_number")
        alert.send_keys("10")
        alert.send_keys(Keys.TAB)
        time.sleep(1)
        self.assertEqual(
            self.browser.find_element_by_id("prime_number").text,
            "Highest prime number lower than 10: 7"
        )

    # when user input negative integer
    # gives the message prime number must be greater than 1
    def test_when_user_enter_input_invalid_number(self):
        self.browser.get(self.live_server_url)
        alert = self.browser.find_element_by_id("input_number")
        alert.send_keys("-10")
        alert.send_keys(Keys.TAB)
        time.sleep(1)
        self.assertEqual(
            self.browser.find_element_by_id("prime_number").text,
            "-10 is NOT a Natural Number, A Prime Number must be greater than 1"
        )

    # when user gives string or special characters
    # response please enter positive integer
    def test_when_user_enter_string_and_special_char(self):
        self.browser.get(self.live_server_url)
        alert = self.browser.find_element_by_id("input_number")
        alert.send_keys("Ancbd@")
        alert.send_keys(Keys.TAB)
        time.sleep(1)
        response = self.browser.find_element_by_id("prime_number").text
        print("", response)
        self.assertEqual(
                self.browser.find_element_by_id("prime_number").text,
                "please enter positive integer . Ancbd@ not a number"
            )