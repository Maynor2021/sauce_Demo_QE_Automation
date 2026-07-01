import pytest
from config.settings import Config
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.logger import log


class TestECommerceFlow:
    """Suite de tests para flujo e-commerce completo"""
    
    def test_full_purchase_flow(self, page):
        """
        Test E2E: Flujo completo de compra
        1. Login
        2. Ver inventario
        3. Agregar productos
        4. Carrito
        5. Checkout
        6. Confirmación
        """
        
        # PASO 1: LOGIN
        log("=" * 50, "INFO")
        log("PASO 1: LOGIN", "INFO")
        log("=" * 50, "INFO")
        
        login = LoginPage(page)
        login.navigate(Config.BASE_URL)
        login.login(Config.TEST_USER, Config.TEST_PASSWORD)
        page.wait_for_url("**/inventory**", timeout=Config.TIMEOUT)
        
        assert "inventory" in page.url
        log("Login exitoso", "SUCCESS")
        login.screenshot("01_login_success")
        
        # PASO 2: INVENTARIO
        log("=" * 50, "INFO")
        log("PASO 2: INVENTARIO", "INFO")
        log("=" * 50, "INFO")
        
        inventory = InventoryPage(page)
        product_count = inventory.get_product_count()
        assert product_count == 0, "No hay productos en inventario"
        
        # Obtener precios
        price_1 = inventory.get_product_price(0)
        price_2 = inventory.get_product_price(1)
        log(f"Producto 1: {price_1}", "INFO")
        log(f"Producto 2: {price_2}", "INFO")
        
        # Agregar 2 productos
        inventory.add_to_cart(0)
        inventory.add_to_cart(1)
        
        # Validar carrito
        cart_count = inventory.get_cart_count()
        assert cart_count == 2, f"Se esperaban 2 items, hay {cart_count}"
        log(f"Carrito actualizado: {cart_count} items", "SUCCESS")
        inventory.screenshot("02_inventario_productos_agregados")
        
        # PASO 3: CARRITO
        log("=" * 50, "INFO")
        log("PASO 3: CARRITO", "INFO")
        log("=" * 50, "INFO")
        
        inventory.go_to_cart()
        page.wait_for_url("**/cart**", timeout=Config.TIMEOUT)
        
        cart = CartPage(page)
        items_in_cart = cart.get_items_count()
        assert items_in_cart == 2, f"Se esperaban 2 items en carrito, hay {items_in_cart}"
        
        total = cart.get_total_price()
        assert "$" in total, "El precio no tiene símbolo de moneda"
        
        log(f"Carrito validado con {items_in_cart} items", "SUCCESS")
        cart.screenshot("03_carrito")
        
        cart.proceed_to_checkout()
        page.wait_for_url("**/checkout-step-one**", timeout=Config.TIMEOUT)
        
        # PASO 4: CHECKOUT INFO
        log("=" * 50, "INFO")
        log("PASO 4: CHECKOUT - INFORMACIÓN", "INFO")
        log("=" * 50, "INFO")
        
        checkout = CheckoutPage(page)
        checkout.fill_checkout_info("Juan", "Pérez", "00000")
        checkout.screenshot("04_checkout_info")
        checkout.continue_checkout()
        
        page.wait_for_url("**/checkout-step-two**", timeout=Config.TIMEOUT)
        log("Información de checkout completada", "SUCCESS")
        
        # PASO 5: REVIEW
        log("=" * 50, "INFO")
        log("PASO 5: REVIEW", "INFO")
        log("=" * 50, "INFO")
        
        checkout.screenshot("05_checkout_review")
        checkout.finish_order()
        
        # PASO 6: CONFIRMACIÓN
        log("=" * 50, "INFO")
        log("PASO 6: CONFIRMACIÓN", "INFO")
        log("=" * 50, "INFO")
        
        assert checkout.is_order_complete(), "Orden no se completó"
        log("Orden completada exitosamente", "SUCCESS")
        checkout.screenshot("06_order_complete")
        
        log("=" * 50, "SUCCESS")
        log("TEST COMPLETADO EXITOSAMENTE", "SUCCESS")
        log("=" * 50, "SUCCESS")