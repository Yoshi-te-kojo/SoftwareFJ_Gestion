import logging

# Configuración del sistema de logs
logging.basicConfig(
    filename='software_fj.logs',
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    encoding='utf-8'
)

def log_event(mensaje: str, nivel: str = "info"):
    if nivel == "error":
        logging.error(mensaje)
        print(f"🔴 ERROR: {mensaje}")
    else:
        logging.info(mensaje)
        print(f"📝 {mensaje}")
