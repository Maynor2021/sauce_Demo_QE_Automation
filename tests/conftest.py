import pytest
from playwright.sync_api import sync_playwright
from config.settings import Config
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.fixture(scope="session")
def browser():
    """Crea un browser una sola vez para toda la sesión"""
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=Config.HEADLESS)
    yield browser
    browser.close()

@pytest.fixture
def page(browser):
    """Crea una nueva página para cada test"""
    page = browser.new_page()
    page.set_default_timeout(Config.TIMEOUT)
    yield page
    page.close()

@pytest.fixture
def login_page(page):
    """Proporciona una instancia de LoginPage"""
    page.goto(Config.BASE_URL)
    return LoginPage(page)

@pytest.fixture
def inventory_page(page):
    """Proporciona una instancia de InventoryPage"""
    page.goto(f"{Config.BASE_URL}/inventory.html")
    return InventoryPage(page)

@pytest.fixture
def cart_page(page):
    """Proporciona una instancia de CartPage"""
    page.goto(f"{Config.BASE_URL}/cart.html")
    return CartPage(page)

@pytest.fixture
def checkout_page(page):
    """Proporciona una instancia de CheckoutPage"""
    page.goto(f"{Config.BASE_URL}/checkout-step-one.html")
    return CheckoutPage(page)