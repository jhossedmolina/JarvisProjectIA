# JarvisProjectIA

**JARVIS** - Just A Rather Very Intelligent System

Un asistente virtual por voz desarrollado en Python, inspirado en el asistente de inteligencia artificial de Iron Man.

## 📋 Características

- 🎤 Reconocimiento de voz en español
- 🔊 Respuestas por voz
- ⏰ Consulta de hora y fecha
- 🔍 Búsquedas en internet
- 🌐 Apertura de sitios web (YouTube, Google)
- 💻 Información del sistema

## 🔧 Requisitos Previos

- Python 3.7 o superior
- Micrófono funcional
- Conexión a internet (para reconocimiento de voz)
- Sistema operativo: Windows, macOS o Linux

### Dependencias del Sistema

#### En Ubuntu/Debian:
```bash
sudo apt-get update
sudo apt-get install python3-pip python3-dev portaudio19-dev
```

#### En macOS:
```bash
brew install portaudio
```

#### En Windows:
- Descargar e instalar Python desde [python.org](https://www.python.org/downloads/)
- PyAudio viene precompilado con pip

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/jhossedmolina/JarvisProjectIA.git
cd JarvisProjectIA
```

### 2. Crear un entorno virtual (recomendado)

```bash
python3 -m venv venv
```

Activar el entorno virtual:

- **Linux/macOS:**
  ```bash
  source venv/bin/activate
  ```

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

**Nota:** Si tienes problemas instalando PyAudio en Windows, puedes descargar el wheel precompilado apropiado para tu versión de Python desde [aquí](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio). Descarga el archivo que corresponda a tu versión de Python y arquitectura (32 o 64 bits) y luego:

```bash
pip install nombre_del_archivo_descargado.whl
```

Por ejemplo, para Python 3.9 de 64 bits:
```bash
pip install PyAudio‑0.2.11‑cp39‑cp39‑win_amd64.whl
```

## ▶️ Cómo Ejecutar la Aplicación

### Método 1: Ejecución directa

```bash
python jarvis.py
```

### Método 2: Como script ejecutable (Linux/macOS)

```bash
chmod +x jarvis.py
./jarvis.py
```

## 🎯 Comandos Disponibles

Una vez que Jarvis esté ejecutándose, puedes usar los siguientes comandos de voz:

| Comando | Descripción |
|---------|-------------|
| "Hola" / "Buenos días" | Saludo inicial |
| "¿Qué hora es?" | Consultar la hora actual |
| "¿Qué día es hoy?" / "Fecha" | Consultar la fecha actual |
| "Busca [tema]" | Buscar algo en Google |
| "Abre YouTube" | Abrir YouTube en el navegador |
| "Abre Google" | Abrir Google en el navegador |
| "Información del sistema" | Ver información del sistema operativo |
| "Ayuda" | Ver lista de comandos |
| "Salir" / "Adiós" | Cerrar el asistente |

## 📝 Ejemplo de Uso

```
================================================
JARVIS - Just A Rather Very Intelligent System
================================================
Jarvis: Hola! Soy Jarvis, tu asistente virtual. ¿En qué puedo ayudarte?
Jarvis: Di 'ayuda' para ver los comandos disponibles
Listening...
You: hola jarvis
Jarvis: Hola! Soy Jarvis. ¿En qué puedo ayudarte?
Listening...
You: qué hora es
Jarvis: Son las 15:30
Listening...
```

## 🔧 Solución de Problemas

### El micrófono no funciona
- Verifica que tu micrófono esté correctamente conectado
- Asegúrate de dar permisos de micrófono a la aplicación
- Prueba ejecutando: `python -m speech_recognition` para verificar el micrófono

### Error al instalar PyAudio
- En Windows, usa el wheel precompilado mencionado en la instalación
- En Linux, instala las dependencias del sistema primero
- En macOS, instala portaudio con Homebrew

### No reconoce comandos de voz
- Habla claramente y cerca del micrófono
- Asegúrate de tener conexión a internet
- Verifica que el micrófono esté configurado como dispositivo por defecto

### Problemas con pyttsx3
Si tienes problemas con la voz en Linux:
```bash
sudo apt-get install espeak
```

## 🤝 Contribuir

Las contribuciones son bienvenidas! Si quieres mejorar Jarvis:

1. Haz un Fork del proyecto
2. Crea una rama para tu función (`git checkout -b feature/nueva-funcion`)
3. Commit tus cambios (`git commit -m 'Agregar nueva función'`)
4. Push a la rama (`git push origin feature/nueva-funcion`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 👨‍💻 Autor

- [@jhossedmolina](https://github.com/jhossedmolina)

## 🙏 Agradecimientos

- Inspirado en JARVIS de Iron Man
- Construido con Python y librerías de código abierto
