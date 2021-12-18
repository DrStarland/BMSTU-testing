import pytest
from pytest_bdd import scenario, given, when, then
from selenium import webdriver
 
from pytest_bdd import given, when, then, scenario, parsers


@pytest.fixture
def browser(request):
    br = webdriver.Firefox()
    yield br
    br.quit()
    
@scenario("setRating.feature", "User finds product by filter and sets rating to it")
def test_user():
    pass

@given("User visits the login page")
def visit_page(browser):
    browser.get("https://localhost:8000")

@given(parsers.parse("He entered {username} username"))
def enter_login(username):
    assert isinstance(username, str)
    assert 2 <= len(username) <= 20

@given(parsers.parse("He entered {password} password"))
def enter_password(password):
    assert isinstance(password, str)
    assert 6 <= len(password) <= 25

@when("He clicked on Products Catalogue")
def visit_page_products(browser):
    browser.get("https://localhost:8000/api/v1/Products/")

@when(parsers.parse("He clicked on the filter, he saw products for {price:d} price"))
def visit_page_filter_products(price):
    assert isinstance(price, int) and price > 0

@when(parsers.parse("He clicked on Product {number:d} with name {productName}"))
def visit_page_one_product(number, productName):
    assert isinstance(number, int)
    assert number > 0
    assert productName == 'kistochka'

@then(parsers.parse("He set {ratingvalue:d} rating to it"))
def set_rating_to_product(ratingvalue):
    assert isinstance(ratingvalue, int) and 0 < ratingvalue <= 10
