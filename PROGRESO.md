# Bot Estática Vital Salud — Progreso

## Qué queremos hacer
Bot para Instagram que:
- Detecta comentarios en los posts
- Le manda un DM automático a la persona con su nombre
- Responde según el tratamiento mencionado (depilación, facial, masaje, corporal)
- Termina con una pregunta abierta para que el setter cierre la venta

## Archivos creados
Todos están en: C:\Users\IK\estatica-bot\

- bot.py           → el código del bot
- .env             → aquí van las credenciales (token + ID de Instagram)
- requirements.txt → librerías que necesita el bot

## Pasos completados
- [x] Código del bot listo
- [x] Archivos del proyecto creados
- [x] Python instalado (versión 3.14, con "Add Python to PATH" marcado)
- [x] pip install -r requirements.txt ejecutado correctamente
- [x] App creada en developers.facebook.com (nombre: Estatica Vital Bot)
- [x] Instagram cambiado a cuenta de Empresa
- [x] Token de acceso (PAGE_ACCESS_TOKEN) conseguido y pegado en el archivo .env
      → Se obtuvo desde: developers.facebook.com/tools/explorer
      → "Obtener token de acceso a la página" con la app Estatica Vital Bot

## Pasos pendientes
- [ ] Conseguir el ID de Instagram (Configuración → Cuenta → ID de cuenta profesional)
- [ ] Pegar ese ID en el archivo .env donde dice IG_ACCOUNT_ID
- [ ] Guardar el archivo .env
- [ ] Crear cuenta en railway.app y subir el proyecto
- [ ] Configurar el Webhook en Meta apuntando a la URL de Railway
- [ ] Probar que funcione

## Siguiente paso cuando regreses
Buscar en Instagram → Configuración → Cuenta → "ID de cuenta profesional"
Copiar ese número y pegarlo en el archivo .env donde dice IG_ACCOUNT_ID=
Luego guardar el archivo .env con Ctrl+S.
