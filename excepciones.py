#excepciones.py - Definición de excepciones personalizadas para el sistema de gestión de reservas
class ErrorSoftwareFJ(Exception):
    """Excepción base para todo el sistema."""
    pass

#Excepciones específicas para validación de datos y operaciones de reserva
class ErrorValidacion(ErrorSoftwareFJ):
    """Error en validación de datos."""
    pass

#Error específico para operaciones de reserva
class ErrorReserva(ErrorSoftwareFJ):
    """Error específico en operaciones de reserva."""
    pass
    
class ClienteExistenteError(ErrorValidacion):
    """El cliente ya se encuentra registrado."""
    pass

class DatosInvalidosError(ErrorValidacion):
    """Los datos ingresados son inválidos."""
    pass

class ServicioNoDisponibleError(ErrorReserva):
    """El servicio solicitado no está disponible."""
    pass

class ReservaNoEncontradaError(ErrorReserva):
    """La reserva solicitada no existe."""
    pass


class HabitacionOcupadaError(ErrorReserva):
    """La habitación ya está ocupada."""
    pass
