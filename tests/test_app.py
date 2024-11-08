import pytest
from app import app

@pytest.fixture
def client():
  with app.test_client() as client:
    yield client

def test_translate_valid_request(client):
  response = client.post('/translate', json={
    'fromLanguage': 'Español',
    'toLanguage': 'English',
    'text': 'Hola'
  })
  assert response.status_code == 200
  assert 'translated_text' in response.get_json()

def test_translate_auto_language_detection(client):
  response = client.post('/translate', json={
    'fromLanguage': 'auto',
    'toLanguage': 'English',
    'text': 'Hola'
  })
  assert response.status_code == 200
  data = response.get_json()
  assert 'translated_text' in data

def test_translate_missing_from_language(client):
  response = client.post('/translate', json={
    'fromLanguage': '',
    'toLanguage': 'English',
    'text': 'Hola'
  })
  assert response.status_code == 400
  json_data = response.get_json()
  assert 'error' in json_data
  assert json_data['error'] == "The 'fromLanguage' field cannot be empty."

def test_translate_missing_to_language(client):
  response = client.post('/translate', json={
    'fromLanguage': 'Español',
    'toLanguage': '',
    'text': 'Hola'
  })
  assert response.status_code == 400
  json_data = response.get_json()
  assert 'error' in json_data
  assert json_data['error'] == "The 'toLanguage' field cannot be empty."

def test_translate_missing_text(client):
  response = client.post('/translate', json={
    'fromLanguage': 'Español',
    'toLanguage': 'English',
    'text': ''
  })
  assert response.status_code == 400
  json_data = response.get_json()
  assert 'error' in json_data
  assert json_data['error'] == "The 'text' field cannot be empty."

def test_translate_same_language(client):
  response = client.post('/translate', json={
    'fromLanguage': 'Español',
    'toLanguage': 'Español',
    'text': 'Hola'
  })
  assert response.status_code == 200
  json_data = response.get_json()
  assert json_data['translated_text'] == 'Hola'
  assert json_data['total_tokens'] == 0
