import os

# Crear archivos (sin las carpetas, ya existen)
archivos = [
    "pages/__init__.py",
    "pages/base_page.py",
    "pages/login_page.py",
    "pages/inventory_page.py",
    "pages/cart_page.py",
    "pages/checkout_page.py",
    "tests/__init__.py",
    "tests/conftest.py",
    "tests/test_full_flow.py",
    "config/__init__.py",
    "config/settings.py",
    "utils/__init__.py",
    "utils/logger.py",
    ".env",
    "pytest.ini",
    "requirements.txt"
]

for archivo in archivos:
    open(archivo, 'a').close()
    print(f"✓ Creado: {archivo}")

print("\n✓ ¡Proyecto creado exitosamente!")