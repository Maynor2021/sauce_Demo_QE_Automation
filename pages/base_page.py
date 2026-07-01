from playwright.sync_api import Page
from config.settings import Config
from utils.logger import log
import os
class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.timeout = Config.TIMEOUT
        
    def navigate(self, url: str):
        log(f"Navegando a {url}...", "INFO")
        self.page.goto(url, timeout=self.timeout)

    def click(self, selector: str):
        log(f"Haciendo click en {selector}...", "INFO")
        self.page.locator(selector).click(timeout=self.timeout)
        
    def fill(self, selector: str, text: str):
         log(f"Llenando {selector} con '{text}'")
         self.page.locator(selector).fill(text)
         
    def get_text(self, selector: str) -> str:
        return self.page.locator(selector).text_content()
    
    
    
    
    def is_visible(self, selector: str) -> bool:
        return self.page.locator(selector).is_visible()
    
    def wait_for(self, selector: str):
        log(f"Esperando {selector}")
        self.page.locator(selector).wait_for(timeout=self.timeout)
    
    def screenshot(self, name: str):
        os.makedirs("screenshots", exist_ok=True)
        self.page.screenshot(path=f"screenshots/{name}.png")
        log(f"Screenshot guardado: {name}", "SUCCESS")