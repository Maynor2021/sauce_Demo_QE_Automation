from pages.base_page import BasePage
from utils.logger import log

class CheckoutPage(BasePage):
    # Step One
    FIRST_NAME = "#first-name"
    LAST_NAME = "#last-name"
    POSTAL_CODE = "#postal-code"
    CONTINUE_BTN = "#continue"
    
    # Step Two (Review)
    FINISH_BTN = "#finish"
    ORDER_COMPLETE = ".complete-header"
    
    def fill_checkout_info(self, first_name: str, last_name: str, 
                          postal_code: str):
        """Llena información del checkout"""
        log(f"Llenando información: {first_name} {last_name}")
        self.fill(self.FIRST_NAME, first_name)
        self.fill(self.LAST_NAME, last_name)
        self.fill(self.POSTAL_CODE, postal_code)
    
    def continue_checkout(self):
        """Continúa con el checkout"""
        log("Continuando con checkout")
        self.click(self.CONTINUE_BTN)
    
    def finish_order(self):
        """Finaliza la orden"""
        log("Finalizando orden")
        self.click(self.FINISH_BTN)
    
    def is_order_complete(self) -> bool:
        """Verifica si la orden se completó"""
        return self.is_visible(self.ORDER_COMPLETE)