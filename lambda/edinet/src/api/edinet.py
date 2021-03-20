import requests
from datetime import date
import urllib.parse

def get_count(target_date=None):
  if target_date is None:
    target_date = date.today()

  payload = {
    'date': target_date.strftime('%Y-%m-%d')
  }
  r = __request('documents.json', params=payload)

  if r.status_code != 200:
    raise RuntimeError('API call failed')

  body = r.json()
  return body['metadata']['resultset']['count']

def get_documents(target_date=None):
  if target_date is None:
    target_date = date.today()

  payload = {
    'date': target_date.strftime('%Y-%m-%d'),
    'type': 2
  }
  r = __request('documents.json', params=payload)

  if r.status_code != 200:
    raise RuntimeError('API call failed')

  body = r.json()
  return body['results']

def get_document(document_id):
  payload = {
    'type': 1
  }
  r = __request('documents/' + document_id, params=payload)

  if r.status_code != 200:
    raise RuntimeError('API call failed')

  zipfilename = '/tmp/' + document_id + '.zip'
  with open(zipfilename, 'wb') as f:
    for chunk in r.iter_content(chunk_size=1024):
      if chunk:
        f.write(chunk)
        f.flush()

  return zipfilename

def __request(path, params={}):
  return requests.get(__fullurl(path), params=params)

def __fullurl(path):
  return urllib.parse.urljoin('https://disclosure.edinet-fsa.go.jp/api/v1/', path)
