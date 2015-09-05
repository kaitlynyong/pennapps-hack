from flask import Flask
#from spacy.en import English
from pdfs import (request_form)

#nlp = English()
app = Flask(__name__)
#app.config['DEBUG'] = True

@app.route('/<form>')
def app_request_form(form):
  return request_form(form)

if __name__ == '__main__':
  app.run()