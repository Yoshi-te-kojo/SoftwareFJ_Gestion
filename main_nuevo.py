from models.cliente import Cliente
from models.servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from models.reserva import Reserva
from models.excepciones import *
from utils.logger import log_event

def main():
    log_event("=== INICIO DEL SISTEMA SOFTWARE FJ ===")
    
    clientes = []
    servicios = []
    reservas = []

    print("\n🚀 SISTEMA DE GESTIÓN SOFTWARE FJ\n")

    try:
        # 1. Cliente válido
        c1 = Cliente("C001", "Juan Pérez", "juan.perez@email.com", "3001234567")
        clientes.append(c1)
        log_event(f"Cliente registrado: {c1}")

        # 2. Prueba de excepción (cliente inválido)
        try:
            Cliente("C2", "Ana", "anaemail.com", "123")
        except ClienteInvalido as e:
            log_event(str(e), "error")

        # 3. Servicios
        s1 = ReservaSala("S001", "Sala Creativa", 45000, 15)
        s2 = AlquilerEquipo("S002", "Laptop Dell", 85000, "Portátil")
        s3 = AsesoriaEspecializada("S003", "Consultoría IA", 120000, "Dr. Martínez")
        servicios.extend([s1, s2, s3])
        log_event("3 Servicios creados correctamente")

        # 4. Reservas
        r1 = Reserva("R001", c1, s1, 8)
        r1.confirmar(es_fin_de_semana=True)
        reservas.append(r1)

        r2 = Reserva("R002", c1, s2, 24)
        r2.confirmar(cantidad=1)
        reservas.append(r2)

        # Resumen final
        print("\n" + "="*60)
        print("RESUMEN FINAL")
        print("="*60)
        print(f"Clientes: {len(clientes)}")
        print(f"Servicios: {len(servicios)}")
        print(f"Reservas: {len(reservas)}")
        print("="*60)

    except Exception as e:
        log_event(f"Error crítico: {e}", "error")
    finally:
        log_event("=== FIN DEL SISTEMA ===")

if __name__ == "__main__":
    main()
