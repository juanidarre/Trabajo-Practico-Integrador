# Stack Tecnológico - Chatbot de Gestión de Vacaciones

Para la implementación de la solución automatizada, se selecciono un stack de herramientas que garantiza escalabilidad, facilidad de integración y robustez.

## 1. Lenguaje de Programación: Python
Se elige **Python** debido a su sintaxis clara y su amplio ecosistema de librerías para el desarrollo de chatbots y manejo de datos. Su versatilidad permite implementar la lógica de la máquina de estados de forma eficiente.

## 2. Framework: Django
Se utilizará el framework **Django** para gestionar la lógica de negocio y la interacción con la base de datos. Django provee un panel de administración robusto que facilita la simulación de las tareas del "Jefe" o "RRHH" para aprobar solicitudes.

## 3. Plataforma del Bot: Telegram API
Se ha seleccionado **Telegram** como interfaz de usuario por las siguientes razones:
- API gratuita y bien documentada.
- Soporte para botones personalizados (Inline Keyboards) que facilitan la toma de decisiones del jefe.
- Facilidad de acceso para el empleado desde cualquier dispositivo móvil o web.

## 4. Persistencia de Datos: SQLite / PostgreSQL
Para cumplir con el requisito de persistencia, el bot consultará una base de datos relacional donde se almacenarán los legajos, saldos de días y los estados de cada solicitud.

## 5. Herramientas de IA
Se utilizó **NotebookLM (Gemini)** como asistente de consultoría para:
- Validar la coherencia de los diagramas BPMN 2.0.
- Diseñar la matriz de transición de la máquina de estados.
- Estructurar el diccionario de datos siguiendo los estándares solicitados.
