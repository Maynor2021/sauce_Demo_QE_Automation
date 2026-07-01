import os 
from dotenv import load_dotenv

load_dotenv()
# Configuración de la URL base y credenciales
class Config:
    BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com")
    HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"
    TEST_USER = os.getenv("TEST_USER", "standard_user")
    TEST_PASSWORD = os.getenv("TEST_PASSWORD", "secret_sauce")
    TIMEOUT = int(os.getenv("TIMEOUT", "5000"))
    