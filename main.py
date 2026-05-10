from entidades import Cliente, ReservaSala, AlquilerEquipo, Asesoria
from gestion import GestorReservas
from excepciones import ErrorReserva, ErrorValidacion

#Función para ejecutar la simulación de reservas con manejo de excepciones
def ejecutar_simulacion():
    gestor = GestorReservas()

    #Clientes válidos e inválidos
    try:
        c1 = Cliente("Juan Perez ", 1)
        print(f"Cliente creado: {c1}")
    except ErrorValidacion as e:
        print(f"Error creando cliente c1: {e}")

    #Inválido por: nombre vacío
    try:
        c2 = Cliente("", 2)  
    except ErrorValidacion as e:
        print(f"Error creando cliente c2: {e}")

    #Inválido por: ID negativo
    try:
        c3 = Cliente("Ana Ramirez", -5)  
    except ErrorValidacion as e:
        print(f"Error creando cliente c3: {e}")

    c4 = Cliente("Luis Gómez", 3)
    c5 = Cliente("Marta Díaz", 4)

    #Sección sobre servicios válidos e inválidos
    try:
        s1 = ReservaSala(1, "Sala A", 100)
        print(f"Servicio creado: {s1.descripcion()}")
    except ErrorValidacion as e:
        print(f"Error creando servicio s1: {e}")

    try:
        s2 = AlquilerEquipo(2, "PC Gamer", 150)
        print(f"Servicio creado: {s2.descripcion()}")
    except ErrorValidacion as e:
        print(f"Error creando servicio s2: {e}")

    try:
        s3 = Asesoria(3, "Consultoría TI", 250)
        print(f"Servicio creado: {s3.descripcion()}")
    except ErrorValidacion as e:
        print(f"Error creando servicio s3: {e}")

    #Inválido por : nombre vacío
    try:
        s4 = ReservaSala(4, "", 80)  
    except ErrorValidacion as e:
        print(f"Error creando servicio s4: {e}")

    #Inválido por: precio negativo
    try:
        s5 = AlquilerEquipo(5, "Proyector", -50)  
    except ErrorValidacion as e:
        print(f"Error creando servicio s5: {e}")

    #Lista de operaciones (cliente, servicio, duración)
    operaciones = [
        (c1, s1, 2),      # válida
        (c4, s2, 3),      # válida
        (c5, s3, 1),      # válida
        (c1, s1, 0),      # inválida (duración 0)
        (c1, None, 2),    # inválida (servicio None)
        (None, s2, 1),    # inválida (cliente None)
        (c1, s3, -1),     # inválida (duración negativa)
        (c4, s2, 2),      # válida
        (c5, s1, 5),      # válida
        (c1, s3, 3),      # válida
    ]

    #Iterar sobre las operaciones y manejar excepciones
    #Cada operación se intenta realizar y se capturan errores específicos de reserva y validación
    #También se captura cualquier error inesperado para asegurar que el programa no falle abruptamente
    for i, (cli, serv, dur) in enumerate(operaciones, 1):
        print(f"\nOperación {i}: Reservar servicio")
        try:
            reserva = gestor.crear_reserva(cli, serv, dur)
            print(f"Reserva exitosa: {reserva}")
            print(f"Costo total: ${reserva.costo_total():.2f}")
        except ErrorReserva as e:
            print(f"Error controlado en reserva: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

#Intentar cancelar una reserva válida y una no existente
if __name__ == "__main__":
    ejecutar_simulacion()