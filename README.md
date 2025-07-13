# 🚀 Rocket Launch Bot

Un bot de Telegram que ayuda a detectar el **frame exacto en el que despega un cohete**, utilizando un sistema interactivo tipo búsqueda binaria (bisección).

---

## 🧠 Funcionalidad

- Comando `/start` para iniciar la conversación.
- Comando `/launch` para comenzar la búsqueda del momento del despegue.
- El bot muestra un fotograma del vídeo y pregunta: _¿Ha despegado ya el cohete?_
- El usuario responde con botones interactivos (`Sí` / `No`).
- A través de un algoritmo de bisección, el bot identifica con precisión el frame en el que se produce el lanzamiento.

---

## 📦 Tecnologías utilizadas

- **Python 3.10+**
- **[python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)** (v20+)
- **httpx** – Cliente HTTP para conectarse a la API FrameX
- **Pillow (PIL)** – Para tratar imágenes desde la API
- **FrameX API** – Para obtener los frames del vídeo del lanzamiento

---

## 📁 Estructura del proyecto

rocket-launch-bot/
├── bot/
│ ├── bisector.py # Lógica de la API FrameX y el algoritmo de bisección
│ └── handlers.py # Comandos, botones y control del flujo del bot
├── main.py # Punto de entrada del bot
├── config.py # Configuración y token del bot
├── requirements.txt # Dependencias del proyecto
└── README.md # Documentación

---

## 🔧 Instalación

```bash
git clone git@github.com:AlexaGSC/rocket-launch-bot.git
cd rocket-launch-bot
python3 -m venv avenv
source avenv/bin/activate
pip install -r requirements.txt
```

## 🔐 Configuración del Token de Telegram

Para que el bot funcione, necesitas un token de autenticación de Telegram. Aquí te explico cómo obtenerlo y configurarlo correctamente.

### 1. Obtén tu token con BotFather

1. Abre Telegram y busca el usuario `@BotFather`.
2. Escribe `/start` para comenzar.
3. Escribe `/newbot` y sigue las instrucciones:
   - Dale un nombre a tu bot.
   - Elige un nombre de usuario único (que termine en `bot`, como `rocketHelperBot`).
4. BotFather te enviará un **token**, algo como:
    123456789:ABCDefGhIjKlMnOpQrStUvWxYz

¡Guárdalo!

---

### 2. Crea el archivo `.env`

En la **raíz del proyecto**, crea un archivo llamado `.env` y añade esta línea con tu token:

BOT_TOKEN=123456789:ABCDefGhIjKlMnOpQrStUvWxYz

(No compartas este token, es confidencial.)

---

### 3. ¿Por qué hay un `config.py`?

El archivo `config.py` se encarga de **leer tu token desde `.env`** de forma segura, sin tener que escribirlo directamente en el código.

### 🚀 Ejecutar el Bot

Con el entorno virtual activado y el `.env` configurado, lanza el bot con:

```bash
python3 main.py

```

Si todo está correcto, deberías ver en la consola:
🚀 Bot is running...

Abre tu bot en Telegram y envía /start o /launch para comenzar la búsqueda del frame exacto del despegue.

### 🧪 Comandos disponibles

- `/start`: Muestra un mensaje de bienvenida.
- `/launch`: Inicia la búsqueda interactiva del momento del despegue.

