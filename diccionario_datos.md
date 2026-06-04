# Diccionario de Datos - Proceso de Vacaciones

Este documento describe la estructura de la base de datos necesaria para el chatbot de gestión de vacaciones.

## Entidad: Empleado
| Campo | Tipo | Longitud | Descripción | Llave |
| :--- | :--- | :--- | :--- | :--- |
| `ID_Empleado` | Número | 10 | Legajo único del trabajador. | PK (Primaria) |
| `Nombre` | Cadena | 50 | Nombre completo del empleado. | |
| `Dias_Disponibles`| Número | 2 | Saldo de días de vacaciones restantes. | |
| `ID_Jefe` | Número | 10 | ID del superior que debe autorizar. | FK (Foránea) |

## Entidad: Solicitud_Vacaciones
| Campo | Tipo | Longitud | Descripción | Llave |
| :--- | :--- | :--- | :--- | :--- |
| `ID_Solicitud` | Número | 10 | Identificador único de la petición. | PK (Primaria) |
| `ID_Empleado` | Número | 10 | Legajo del solicitante. | FK (Foránea) |
| `Fecha_Inicio` | Fecha | 10 | Fecha de inicio (DD/MM/AAAA). | |
| `Fecha_Fin` | Fecha | 10 | Fecha de fin (DD/MM/AAAA). | |
| `Estado` | Cadena | 15 | "Pendiente", "Aprobada" o "Rechazada". | |
