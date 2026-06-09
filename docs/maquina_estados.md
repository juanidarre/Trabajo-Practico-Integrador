# Máquina de Estados - Chatbot de Gestión de Vacaciones

Este documento define la lógica de navegación del bot, permitiendo que el sistema mantenga la trazabilidad de la conversación con el empleado.

## 1. Componentes de la Máquina de Estados
Siguiendo con la teoría, definimos:
- **Estados (S):** Las situaciones posibles del bot (ej: ESPERANDO_LEGAJO).
- **Entradas/Eventos (E):** Lo que el usuario envía o lo que el sistema detecta.
- **Transiciones (T):** Las reglas para pasar de un estado a otro.
- **Acciones (A):** Lo que el bot hace en cada paso (consultar BD, enviar mensaje).

## 2. Matriz de Transiciones
| Estado Actual | Evento / Entrada | Estado Siguiente | Acción (Output) |
| :--- | :--- | :--- | :--- |
| **IDLE (Inicio)** | Usuario saluda o inicia | **ESPERANDO_LEGAJO** | Solicitar número de Legajo. |
| **ESPERANDO_LEGAJO** | Recibe `ID_Empleado` | **VERIFICANDO_SALDO** | Consultar campo `Dias_Disponibles`. |
| **VERIFICANDO_SALDO** | Saldo > 0 | **ESPERANDO_INICIO** | Solicitar `Fecha_Inicio`. |
| **VERIFICANDO_SALDO** | Saldo == 0 | **IDLE** | Notificar rechazo y finalizar. |
| **ESPERANDO_INICIO** | Fecha válida recibida | **ESPERANDO_FIN** | Solicitar `Fecha_Fin`. |
| **ESPERANDO_FIN** | Fecha válida recibida | **ESPERANDO_APROBACION** | Enviar solicitud al Jefe. |
| **ESPERANDO_APROBACION**| Jefe selecciona "Aprobar"| **IDLE** | Actualizar BD y notificar éxito. |
| **ESPERANDO_APROBACION**| Jefe selecciona "Rechazar"| **IDLE** | Notificar rechazo y finalizar. |

## 3. Manejo de Errores (Camino Infeliz)
Para asegurar la robustez del sistema, si el usuario envía un dato inválido (ej: texto en lugar de fecha), la máquina permanecerá en el estado actual y disparará una acción de reintento.
