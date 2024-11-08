from flask import Flask, request, jsonify
from translate import translate_text
from validation import validate_translation_data
from dotenv import load_dotenv
from flask_cors import CORS
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()
app = Flask(__name__)
CORS(app, resources={r"/translate": {"origins": "*"}})

# Define a route for the translation endpoint
@app.route('/translate', methods=['POST'])
def translate():
    try:
        # Get the data from the request POST
        data = request.get_json()

        validation_response = validate_translation_data(data)
        if validation_response:
            return validation_response

        from_language = data['fromLanguage']
        to_language = data['toLanguage']
        text = data['text']

        translation_result = translate_text(from_language, to_language, text)

        # Validate the input data is present
        if 'error' in translation_result:
            logger.error(f"Error en la traducción: {translation_result['error']}")
            return jsonify({'error': 'Error al procesar la traducción. Por favor, intente de nuevo.'}), 500

        # Return both the translated text and tokens used
        return jsonify(translation_result)
    
    except Exception as e:
        logger.exception("Error inesperado en la API de traducción")
        return jsonify({'error': 'Error interno del servidor. Por favor, intente de nuevo más tarde.'}), 500
  
# Route for testing if the server is running
@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Api translate is running'}), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=False)