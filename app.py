from flask import Flask
from spacy import en
from pdfs import (request_form)

app = Flask(__name__)

@app.route('/<form>')
def app_request_form(form):
  return request_form(form)

if __name__ == '__main__':
  #nlp = en.English()
  app.run()