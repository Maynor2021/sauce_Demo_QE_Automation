def log(message: str, level: str = "INFO"):
    """Logger simple para tests"""
    symbols = {
        "INFO": "ℹ️",
        "SUCCESS": "✓",
        "ERROR": "✗",
        "WARNING": "⚠️"
    }
    print(f"{symbols.get(level, '→')} {message}")