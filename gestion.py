import logging
from excepciones import ErrorReserva, ErrorValidacion
from entidades import * 

#Configuración de logging
logging.basicConfig(
    filename='software_fj.log',
    filemode='a',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

#Clase de gestión de reservas
#para manejar la lógica de negocio relacionada con las reservas
class GestorReservas:
    def __init__(self):
        self.reservas = []

    #Método para crear una reserva con manejo de excepciones
    def crear_reserva(self, cliente, servicio, duracion):
        try:
            nueva_reserva = Reserva(cliente, servicio, duracion)
            nueva_reserva.procesar()
        except ErrorValidacion as e:
            logging.error(f"Validación fallida en reserva: {e}")
            raise ErrorReserva("Error al crear reserva debido a datos inválidos.") from e
        except Exception as e:
            logging.error(f"Error inesperado al crear reserva: {e}")
            raise ErrorReserva("Error inesperado al crear reserva.") from e
        else:
            self.reservas.append(nueva_reserva)
            logging.info(f"Reserva creada exitosamente: {nueva_reserva}")
            return nueva_reserva
        finally:
            print(f"Intento de reserva para cliente: {cliente.nombre if cliente else 'Desconocido'} finalizado.")

    #Método para cancelar una reserva con manejo de excepciones
    def cancelar_reserva(self, reserva):
        try:
            if reserva not in self.reservas:
                raise ErrorReserva("La reserva no existe en el sistema.")
            reserva.cancelar()
        except Exception as e:
            logging.error(f"Error al cancelar reserva: {e}")
            raise
        else:
            logging.info(f"Reserva cancelada: {reserva}")
            return reserva