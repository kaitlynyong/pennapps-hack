from spacy.en import English
from slate import PDF
from flask import jsonify

nlp = English()

def request_form(form): 
  pdf = None
  with open('pdfs/' + form + '.pdf') as f:
    pdf = PDF(f)

  if pdf is None: return 1

  ret_doc = {
    "instructions": "",
    "inputs": [
      # {
      #   "type": "checkbox|text|textarea|radio|date|address|signature",
      #   "name": "text",
      #   "value": "text | boolean | number",
      #   "coordinates": ["float", "float"]
      # }
    ]
  }

  u_pdf = unicode('')
  for page in pdf:
    u_pdf += str(page).decode('utf-8')

  tokens = nlp(u_pdf)
  
  #this check should be last
  fill_verbs = set(['enter', 'fill', 'provide', 'list'])
  verbs = [t for t in tokens if (t.pos_ == 'VERB' and str(t.orth_).lower() in fill_verbs)]
  
  actions = []
  for verb in verbs:
    action = ' '.join([t.orth_ for t in verb.subtree])
    actions.append(action)

  for action in actions:
    new_input = {
      "type": "text",
      "name": action,
      "value": None,
      "coordinates": [None, None]
    }
    ret_doc['inputs'].append(new_input)

  return jsonify(ret_doc)