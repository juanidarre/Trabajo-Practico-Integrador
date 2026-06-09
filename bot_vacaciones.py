import os
import json
from datetime import datetime

directorio_actual = os.path.dirname(__file__)
ruta_db = os.path.join(directorio_actual, "data", "base_datos.json")

def cargar_datos():
    if not os.path.exists(ruta_db):
        raise FileNotFoundError(f"Error sistémico: No se encontró la base de datos en: {ruta_db}")
    with open(ruta_db, 'r', encoding='utf-8') as archivo:
        return json.load(archivo)

try:
    db_json = cargar_datos()
    db = db_json["empleados"]
except Exception as e:
    print(f"Error al inicializar el sistema: {e}")
    db = {}

IDLE = "ESPERANDO_LEGAJO"
FECHA_INICIO = "ESPERANDO_INICIO"
FECHA_FIN = "ESPERANDO_FIN"
APROBACION = "ESPERANDO_APROBACION"

class VacacionesBot:
    def __init__(self):
        self.estado_actual = IDLE
        self.datos_solicitud = {}

    def procesar_mensaje(self, mensaje):
        if self.estado_actual == IDLE:
            if mensaje.isdigit():
                legajo = mensaje
                if legajo in db:
                    self.datos_solicitud["legajo"] = legajo
                    saldo = db[legajo]["Días_Disponibles"]
                    print(f"Bot: Hola {db[legajo]['nombre']}. Tienes {saldo} días disponibles.")
                    
                    if saldo > 0:
                        self.estado_actual = FECHA_INICIO
                        return "Por favor, ingresa la fecha de INICIO (formato DD/MM/AAAA):"
                    else:
                        return "No tienes días disponibles para solicitar. Proceso finalizado."
                else:
                    return "Legajo no encontrado en el sistema. Intenta de nuevo:"
            else:
                return "Error: El legajo debe ser un número. Por favor, reingresa:"

        elif self.estado_actual == FECHA_INICIO:
            try:
                datetime.strptime(mensaje, "%d/%m/%Y")
                self.datos_solicitud["inicio"] = mensaje
                self.estado_actual = FECHA_FIN
                return "Fecha registrada. Ahora ingresa la fecha de FIN (formato DD/MM/AAAA):"
            except ValueError:
                return "Error: Formato de fecha inválido. Asegúrate de usar DD/MM/AAAA:"

        elif self.estado_actual == FECHA_FIN:
            try:
                datetime.strptime(mensaje, "%d/%m/%Y")
                self.datos_solicitud["fin"] = mensaje
                self.estado_actual = APROBACION
                return (f"Solicitud procesada para el periodo {self.datos_solicitud['inicio']} al {mensaje}.\n"
                        "Enviada al Jefe para su evaluación. (Escribe 'OK' para simular aprobación)")
            except ValueError:
                return "Error: Formato de fecha inválido. Por favor, usa DD/MM/AAAA:"

        elif self.estado_actual == APROBACION:
            if mensaje.upper() == "OK":
                self.estado_actual = IDLE
                return "¡Vacaciones Aprobadas! Se ha actualizado el registro en el sistema."
            else:
                self.estado_actual = IDLE
                return "Solicitud Rechazada por la Jefatura. Fin del proceso."

if __name__ == "__main__":
    bot = VacacionesBot()
    print("--- Simulador Chatbot Vacaciones (WhatsApp) ---")
    print("Bot: Hola, para comenzar ingresa tu número de legajo:")

    while True:
        entrada = input("Usted: ")
        if entrada.lower() in ["salir", "exit", "quit"]:
            print("Sistema cerrado.")
            break
        respuesta = bot.procesar_mensaje(entrada)
        print(f"Bot: {respuesta}")
