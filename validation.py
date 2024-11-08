from flask import jsonify

def validate_translation_data(data):
  required_fields = {
    "fromLanguage": "The 'fromLanguage' field cannot be empty.",
    "toLanguage": "The 'toLanguage' field cannot be empty.",
    "text": "The 'text' field cannot be empty."
  }

  for field, error_message in required_fields.items():
    if not data.get(field):
      return jsonify({'error': error_message}), 400
  return None