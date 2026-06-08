import json
import os

directorio_actual = os.path.dirname(__file__)
ruta_db = os.path.join(directorio_actual, "data", "base_datos.json")

def cargar_datos():
    # Verificación de robustez: informamos si el archivo no existe antes de que falle
    if not os.path.exists(ruta_db):
        raise FileNotFoundError(f"No se encontró la base de datos en: {ruta_db}")
        
    with open(ruta_db, 'r', encoding='utf-8') as archivo:
        return json.load(archivo)

# Cargar datos
db_json = cargar_datos()
db = db_json["empleados"]

import json

# Simulación de la Base de Datos
db = {
    "101": {"nombre": "Juan Perez", "dias": 15},
    "102": {"nombre": "Ana Lopez", "dias": 0}
}

# Definición de Estados (S)
IDLE = "ESPERANDO_LEGAJO"
VERIFICANDO = "VERIFICANDO_SALDO"
FECHA_INICIO = "ESPERANDO_INICIO"
FECHA_FIN = "ESPERANDO_FIN"
APROBACION = "ESPERANDO_APROBACION"

class VacacionesBot:
    def __init__(self):
        self.estado_actual = IDLE
        self.datos_solicitud = {}

    def procesar_mensaje(self, mensaje):
        # Implementación del "Camino Infeliz": Manejo de errores de entrada
        
        if self.estado_actual == IDLE:
            if mensaje.isdigit(): # Validación: debe ser un número
                legajo = mensaje
                if legajo in db:
                    self.datos_solicitud["legajo"] = legajo
                    saldo = db[legajo]["dias"]
                    print(f"Bot: Hola {db[legajo]['nombre']}. Tienes {saldo} días.")
                    
                    if saldo > 0:
                        self.estado_actual = FECHA_INICIO # Transición (T)
                        return "Por favor, ingresa la fecha de INICIO (DD/MM/AAAA):"
                    else:
                        self.estado_actual = IDLE
                        return "No tienes días disponibles. Proceso finalizado."
                else:
                    return "Legajo no encontrado. Intenta de nuevo:"
            else:
                return "Error: El legajo debe ser un número. Intenta de nuevo:"

        elif self.estado_actual == FECHA_INICIO:
            # Aquí podrías agregar validación de formato de fecha
            self.datos_solicitud["inicio"] = mensaje
            self.estado_actual = FECHA_FIN
            return "Ingresa la fecha de FIN (DD/MM/AAAA):"

        elif self.estado_actual == FECHA_FIN:
            self.datos_solicitud["fin"] = mensaje
            self.estado_actual = APROBACION
            return f"Solicitud enviada al Jefe. Periodo: {self.datos_solicitud['inicio']} al {mensaje}. \n(Escribe 'OK' para simular aprobación del jefe)"

        elif self.estado_actual == APROBACION:
            if mensaje.upper() == "OK":
                self.estado_actual = IDLE
                return "¡Vacaciones Aprobadas! Se ha actualizado el sistema."
            else:
                self.estado_actual = IDLE
                return "Solicitud Rechazada por el superior."

# --- PRUEBA DEL SIMULADOR ---
bot = VacacionesBot()
print("--- Simulador Chatbot Vacaciones (WhatsApp) ---")
print("Bot: Hola, ingresa tu número de legajo:")

while True:
    usuario = input("Usted: ")
    if usuario.lower() == "salir": break
    respuesta = bot.procesar_mensaje(usuario)
    print(f"Bot: {respuesta}")
