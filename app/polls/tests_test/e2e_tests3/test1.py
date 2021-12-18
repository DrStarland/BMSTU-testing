import pytest
from pytest_bdd import scenario, given, when, then
from selenium import webdriver
 
from pytest_bdd import given, when, then, scenario, parsers


@pytest.fixture
def browser(request):
    br = webdriver.Firefox()
    yield br
    br.quit()
    

@scenario("getToCart.feature", "User is getting product to cart")
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

@when(parsers.parse("He clicked on Product {number:d} with name {productName}"))
def visit_page_one_product(number, productName):
    assert isinstance(number, int) and number > 0
    assert productName == 'kistochka'

@then(parsers.parse("He added the product to cart, cartID = {cartID:d}, quantity = {quantity:d}"))
def added_to_cart(cartID, quantity):
    assert isinstance(cartID, int)
    assert quantity == 1

@then(parsers.parse("The total quantity of product became {total_quantity:d}"))
def total_quantity_dec(total_quantity):
    assert total_quantity >= 0
