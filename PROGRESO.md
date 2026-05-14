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
- PROGRESO.md      → este archivo

## Pasos completados
- [x] Código del bot listo
- [x] Archivos del proyecto creados
- [x] Python instalado (versión 3.14, con "Add Python to PATH" marcado)
- [x] pip install -r requirements.txt ejecutado correctamente
- [x] App creada en developers.facebook.com (nombre: Estatica Vital Bot)
- [x] Instagram cambiado a cuenta de Empresa
- [x] Token de acceso (PAGE_ACCESS_TOKEN) conseguido y pegado en .env
- [x] ID de Instagram conseguido y pegado en .env (ID: 1758826807)
- [x] Repositorio de GitHub creado (github.com/madame2804-debug/estatica-bot)
- [x] Git inicializado y commit hecho en la PC
- [x] Repositorio remoto conectado con: git remote add origin

## Pasos pendientes
- [ ] Crear un Personal Access Token en GitHub para poder hacer push
- [ ] Subir el código a GitHub con: git push -u origin master
- [ ] Crear cuenta en railway.app (ya tiene cuenta)
- [ ] Conectar Railway con el repositorio de GitHub
- [ ] Configurar el Webhook en Meta apuntando a la URL de Railway
- [ ] Probar que funcione

## Siguiente paso cuando regreses
Crear el Personal Access Token en GitHub:
1. github.com → foto de perfil arriba derecha → Settings
2. Bajar hasta "Developer settings" (al final del menú izquierdo)
3. Personal access tokens → Tokens (classic) → Generate new token (classic)
4. Darle un nombre, marcar el permiso "repo" y generar
5. Copiar ese token y usarlo como contraseña al hacer: git push -u origin master
