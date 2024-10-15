# API Translate ChatGPT

Esta es una API de traducción que utiliza el modelo GPT-3.5-turbo de OpenAI para traducir texto entre diferentes idiomas. La API está construida con Flask y permite solicitudes de traducción a través de un endpoint.

## Tabla de Contenidos

- [Características](#características)
- [Tecnologías Usadas](#tecnologías-usadas)
- [Instalación](#instalación)
- [Uso](#uso)
- [Ejemplo de Solicitud](#ejemplo-de-solicitud)
- [Manejo de CORS](#manejo-de-cors)
- [Licencia](#licencia)

## Características

- Traducción de texto entre varios idiomas.
- Uso de OpenAI GPT-3.5-turbo para realizar traducciones precisas.
- Soporte para múltiples idiomas.
- Implementación de CORS para permitir solicitudes desde diferentes dominios.

## Tecnologías Usadas

- Python
- Flask
- OpenAI API
- Flask-CORS
- dotenv

## Instalación

1. Clona el repositorio:

  ```bash
  git clone https://github.com/nicolasanhueza/Api-Translate-Chatgpt.git
  cd Api-Translate-Chatgpt
  ```

2. Crea un entorno virtual (opcional pero recomendado):
  
  ```bash
  python -m venv venv
  ```

3. Activa el entorno virtual:

  - En macOS/Linux:

    ```bash
    source venv/bin/activate
    ```
  - En Windows:

    ```bash
    venv\Scripts\activate
    ```

3. Instala las dependencias desde el archivo requirements.txt:

  ```bash
  pip install -r requirements.txt
  ```

4. Configura tus variables de entorno. Crea un archivo .env en la raíz del proyecto y añade tu clave de API de OpenAI:

  `OPENAI_API_KEY=tu_clave_api_aqui`

## USO

  ```bash
  python app.py
  ```

## Ejemplo de Solicitud

- Puedes realizar una solicitud POST a /translate con el siguiente cuerpo JSON:

  ```json
  {
    "fromLanguage": "Español",
    "toLanguage": "English",
    "text": "Hola mundo"
  }

- La respuesta será un JSON que contiene el texto traducido:

  ```json
  {
    "total_tokens": 115,
    "translated_text": "The value now is 363"
  }

## Manejo de CORS

La API está configurada para permitir solicitudes desde cualquier origen. Puedes modificar la configuración de CORS en app.py si es necesario.

## Licencia

Este proyecto está bajo la Licencia MIT.
