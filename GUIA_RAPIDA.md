# Guía Rápida - JarvisProjectIA

## ¿Cómo poner a correr mi aplicación?

### Pasos Rápidos:

1. **Instalar Python** (si no lo tienes):
   - Descarga desde: https://www.python.org/downloads/
   - Asegúrate de marcar "Add Python to PATH" durante la instalación

2. **Abrir la terminal/consola:**
   - Windows: Presiona `Win + R`, escribe `cmd` y presiona Enter
   - Mac: Abre "Terminal" desde Aplicaciones/Utilidades
   - Linux: Presiona `Ctrl + Alt + T`

3. **Navegar a la carpeta del proyecto:**
   ```bash
   cd ruta/a/JarvisProjectIA
   ```

4. **Instalar las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```
   
   Si usas pip3:
   ```bash
   pip3 install -r requirements.txt
   ```

5. **Ejecutar Jarvis:**
   ```bash
   python jarvis.py
   ```
   
   O si usas python3:
   ```bash
   python3 jarvis.py
   ```

6. **¡Listo!** Jarvis comenzará a escuchar tus comandos por voz.

### Solución Rápida de Problemas:

**"pip no se reconoce como comando"**
- Reinstala Python y asegúrate de marcar "Add Python to PATH"

**"Error al instalar PyAudio"**
- Windows: Descarga el archivo .whl desde https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
- Luego ejecuta: `pip install nombre_del_archivo.whl`

**"El micrófono no funciona"**
- Verifica que tu micrófono esté conectado
- Dale permisos a Python para usar el micrófono
- En Windows: Configuración > Privacidad > Micrófono

### Comandos de Voz Básicos:

- "Hola Jarvis"
- "¿Qué hora es?"
- "¿Qué día es hoy?"
- "Busca [cualquier cosa]"
- "Abre YouTube"
- "Salir"

Para más detalles, consulta el archivo README.md
