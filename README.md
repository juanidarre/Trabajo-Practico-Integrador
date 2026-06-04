# TPI - Organización Empresarial: Automatización de Gestión de Vacaciones

## 1. Introducción
Este proyecto busca optimizar el proceso de solicitud y aprobación de vacaciones de los empleados mediante un chatbot administrativo interconectado con una base de datos.

## 2. El Problema (As-Is)
Actualmente, el proceso es manual, basado en correos electrónicos y planillas de Excel dispersas, lo que genera:
*   Falta de visibilidad sobre saldos de días.
*   Demoras en las respuestas.
*   Carga administrativa innecesaria para RRHH.

## 3. Propuesta de Solución (To-Be)
Implementación de un chatbot que:
1.  Verifica automáticamente los días disponibles del empleado.
2.  Solicita las fechas de inicio y fin.
3.  Envía la solicitud al jefe directo para aprobación.
4.  Notifica al empleado y actualiza la base de datos.

## 4. Stack Tecnológico (Preliminar)
*   **Lenguaje:** Python (Framework Django).
*   **Plataforma del Bot:** Telegram API (o Web).
*   **Base de Datos:** SQLite / PostgreSQL.
