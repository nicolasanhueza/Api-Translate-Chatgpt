# API Translate ChatGPT

Esta es una API de traducción que utiliza el modelo GPT-3.5-turbo de OpenAI para traducir texto entre diferentes idiomas. La API está construida con Flask y permite solicitudes de traducción a través de un endpoint.

## Tabla de Contenidos

- [Características](#características)
- [Tecnologías Usadas](#tecnologías-usadas)
- [Instalación](#instalación)
- [Uso](#uso)
- [Ejemplo de Solicitud](#ejemplo-de-solicitud)
- [Ejemplo de Errores](#ejemplo-de-errores)
- [Testing](#testing)
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
Para realizar una solicitud de traducción, envía una solicitud POST a https://api-translate-chatgpt.vercel.app/translate
Solicitud mediante postman:
  - El cuerpo de la solicitud debe estar en formato JSON y configurado como `raw` en el tipo de contenido:

    ```json
    {
      "fromLanguage": "Español",
      "toLanguage": "English",
      "text": "Hola mundo"
    }

  - La respuesta será un JSON que contiene el texto traducido:

    ```json
    {
      "total_tokens": 106,
      "translated_text": "Hello world"
    }

Solicitud mediante otros lenguajes:
  - Solicitud desde React:
  ```jsx
  const translateText = async () => {
  const response = await fetch('https://api-translate-chatgpt.vercel.app/translate', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      fromLanguage: 'Español',
      toLanguage: 'English',
      text: 'Hola mundo',
    }),
  });
  const data = await response.json();
  console.log(data.translated_text); // Debería mostrar "Hello world"
  };
  translateText();
  ```
  - solicitud desde Python:
  ```python
  import requests

  url = "https://api-translate-chatgpt.vercel.app/translate"
  data = {
      "fromLanguage": "Español",
      "toLanguage": "English",
      "text": "Hola mundo"
  }
  headers = {"Content-Type": "application/json"}

  response = requests.post(url, json=data, headers=headers)
  print(response.json().get("translated_text"))
  ```
  - Solicitud desde cURL:
  ```curl
    curl -X POST https://api-translate-chatgpt.vercel.app/translate \
  -H "Content-Type: application/json" \
  -d '{
    "fromLanguage": "Español",
    "toLanguage": "English",
    "text": "Hola mundo"
  }'
  ```

## Ejemplo de Errores

- Solicitud inválida (falta campo):
  ```json
  {
    "fromLanguage": "",
    "toLanguage": "English",
    "text": "Hola mundo"
  }

- Error al procesar la traducción:

  ```json
  {
    "error": "The 'fromLanguage' field cannot be empty."
  }
  

## Testing

Este proyecto utiliza `pytest` para ejecutar las pruebas unitarias. Las pruebas están ubicadas en la carpeta `test`.

Para ejecutar las pruebas:

1. Navega al directorio raíz del proyecto.
2. Ejecuta el siguiente comando:

  ```bash
  pytest test/
  ```

## Manejo de CORS

La API está configurada para permitir solicitudes desde cualquier origen. Puedes modificar la configuración de CORS en app.py si es necesario.

## Licencia

Este proyecto está bajo la Licencia MIT.
