# Manual de Usuario - Chatbot Administrativo de Vacaciones

Este chatbot permite a los empleados de la organización gestionar sus solicitudes de vacaciones de forma autónoma a través de WhatsApp.

## 1. Inicio de Sesión
Para comenzar, el empleado debe enviar un saludo (ej: "Hola" o "Inicio") al número oficial de la empresa. El bot solicitará su **Número de Legajo** para identificarlo en la base de datos.

## 2. Funcionalidades Principales
- **Consulta de Saldo:** Una vez identificado, el bot informará automáticamente cuántos días de vacaciones tiene disponibles el usuario.
- **Solicitud de Fechas:** Si el saldo es suficiente, el bot guiará al usuario para ingresar la `Fecha de Inicio` y la `Fecha de Fin`.
- **Estado de Solicitud:** El empleado recibirá una notificación por WhatsApp una vez que su Jefe haya aprobado o rechazado la petición.

## 3. Guía de Errores Comunes (Camino Infeliz)
- **Legajo Inválido:** Si ingresa un ID que no existe, el bot solicitará que lo reingrese.
- **Formato de Fecha:** Las fechas deben ingresarse en formato `DD/MM/AAAA`. Si se envía texto o un formato distinto, el bot notificará el error y pedirá el dato nuevamente para asegurar la robustez del sistema.
- **Saldo Insuficiente:** Si el usuario intenta pedir más días de los que tiene, el bot finalizará la sesión informando el motivo.
