from pages.base_page import BasePage
from utils.logger import log

class InventoryPage(BasePage):
    # Locators
    INVENTORY_LIST = ".inventory_list"
    PRODUCT_NAME = ".inventory_item_name"
    PRODUCT_PRICE = ".inventory_item_price"
    ADD_TO_CART_BTN = "button[name*='add-to-cart']"
    CART_BADGE = ".shopping_cart_badge"
    CART_LINK = ".shopping_cart_link"
    
    def get_product_count(self) -> int:
        """Obtiene cantidad de productos"""
        products = self.page.locator(self.PRODUCT_NAME)
        count = products.count()
        log(f"Encontrados {count} productos")
        return count
    
    def get_product_price(self, index: int) -> str:
        """Obtiene precio de un producto"""
        prices = self.page.locator(self.PRODUCT_PRICE)
        return prices.nth(index).text_content()
    
    def add_to_cart(self, index: int = 0):
        """Agrega producto al carrito"""
        buttons = self.page.locator(self.ADD_TO_CART_BTN)
        log(f"Agregando producto {index + 1} al carrito")
        buttons.nth(index).click()
    
    def get_cart_count(self) -> int:
        """Obtiene número de items en carrito"""
        if self.is_visible(self.CART_BADGE):
            count = int(self.get_text(self.CART_BADGE))
            log(f"Carrito tiene {count} items")
            return count
        return 0
    
    def go_to_cart(self):
        """Navega al carrito"""
        log("Navegando al carrito")
        self.click(self.CART_LINK)