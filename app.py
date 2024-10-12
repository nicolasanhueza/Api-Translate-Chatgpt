from flask import Flask, request, jsonify
from translate import translate_text
from dotenv import load_dotenv
from flask_cors import CORS
import os

# Load environment variables from .env file
load_dotenv()
app = Flask(__name__)
CORS(app)

# Define a route for the translation endpoint
@app.route('/translate', methods=['POST'])
def translate():
  try:
    # Get the data from the request POST
    data = request.get_json()

    # Print the received data
    print(f"Received data: {data}")

    from_language = data.get('fromLanguage')
    to_language = data.get('toLanguage')
    text = data.get('text')

    # Validate the input data is present
    if not from_language or not to_language or not text:
      return jsonify({'error': 'Missing input data'}), 400
    
    # Call a translation function
    translated_text = translate_text(from_language, to_language, text)

    # Return the translated text as JSON
    return jsonify({'translated_text': translated_text})
  
  except Exception as e:
    return jsonify({'error': str(e)}), 500
  
# Rute of test for verifying the server is running
@app.route('/', methods=['GET'])
def home():
  return jsonify({'message': 'Api translate is running'})

# Execute the app
if __name__ == '__main__':
  app.run(debug=True)
