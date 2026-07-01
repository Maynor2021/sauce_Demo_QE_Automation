from pages.base_page import BasePage
from utils.logger import log

class CartPage(BasePage):
    # Locators
    CART_ITEMS = ".cart_item"
    ITEM_NAME = ".inventory_item_name"
    ITEM_PRICE = ".inventory_item_price"
    SUBTOTAL = ".summary_subtotal_label"
    CHECKOUT_BTN = "#checkout"
    
    def get_items_count(self) -> int:
        """Obtiene cantidad de items en carrito"""
        count = self.page.locator(self.CART_ITEMS).count()
        log(f"Carrito tiene {count} items")
        return count
    
    def get_total_price(self) -> str:
        """Obtiene precio total"""
        total = self.get_text(self.SUBTOTAL)
        log(f"Precio  total: {total}")
        return total
    
    def proceed_to_checkout(self):
        """Continúa al checkout"""
        log("Procediendo al checkout")
        self.click(self.CHECKOUT_BTN)