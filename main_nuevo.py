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

    print("\n🚀 Iniciando Sistema de Gestión Software FJ...\n")

    try:
        # Pruebas de Cliente
        c1 = Cliente("C001", "Juan Pérez", "juan.perez@email.com", "3001234567")
        clientes.append(c1)
        log_event(f"✅ Cliente registrado: {c1}")

        # Prueba de error esperado
        try:
            Cliente("XX", "Ana", "anaemail.com", "123")
        except ClienteInvalido as e:
            log_event(f"❌ Error controlado (esperado): {e}", "error")

        # Servicios
        s1 = ReservaSala("S001", "Sala Creativa", 45000, 12)
        s2 = AlquilerEquipo("S002", "Laptop Dell", 85000, "Portátil")
        s3 = AsesoriaEspecializada("S003", "Consultoría IA", 120000, "Dr. Martínez")
        servicios.extend([s1, s2, s3])

        # Reservas
        r1 = Reserva("R001", c1, s1, 5)
        r1.confirmar(es_fin_de_semana=True)
        reservas.append(r1)

        print("\n" + "="*50)
        print("✅ SISTEMA EJECUTADO CORRECTAMENTE")
        print(f"Clientes: {len(clientes)} | Servicios: {len(servicios)} | Reservas: {len(reservas)}")
        print("="*50)

    except Exception as e:
        log_event(f"❌ Error crítico: {e}", "error")
    finally:
        log_event("=== FIN DE EJECUCIÓN ===")

if __name__ == "__main__":
    main()
