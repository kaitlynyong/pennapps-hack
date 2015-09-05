from spacy.en import English
from slate import PDF

nlp = English()

def request_form(form): 
  pdf = None
  with open('pdfs/' + form + '.pdf') as f:
    pdf = PDF(f)

  if pdf is None: return 1

  u_pdf = unicode('')
  for page in pdf:
    u_pdf += str(page).decode('utf-8')

  tokens = nlp(u_pdf)
  
  #this check should be last
  fill_verbs = set(['enter', 'fill', 'provide', 'list'])
  verbs = [t.orth_ for t in tokens if (t.pos_ == 'VERB' and str(t.orth_).lower() in fill_verbs)]
  
  actions = []
  for token in tokens:
    if token.pos_ == 'NOUN' and token.head.orth_ in verbs:
      actions.append(unicode(token.head.orth_) + u' ' + unicode(token.orth_))

  return str(unicode(actions))