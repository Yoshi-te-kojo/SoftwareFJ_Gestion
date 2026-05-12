import logging
from datetime import datetime

# Configuración del logger
logging.basicConfig(
    filename='logs/logs.log',
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    encoding='utf-8'
)

def log_event(mensaje: str, nivel: str = "info"):
    """Función para registrar eventos y errores"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if nivel == "error":
        logging.error(mensaje)
        print(f"🔴 ERROR | {mensaje}")
    elif nivel == "warning":
        logging.warning(mensaje)
        print(f"⚠️  WARNING | {mensaje}")
    else:
        logging.info(mensaje)
        print(f"📝 INFO | {mensaje}")
