from spacy.en import English
nlp = English()

def request_form(form):
  test_sentence = unicode("Enter your TIN in the appropriate box. The TIN provided must match the name given on line 1 to avoid backup withholding. For individuals, this is generally your social security number (SSN). However, for a resident alien, sole proprietor, or disregarded entity, see the Part I instructions on page 3. For other entities, it is your employer identification number (EIN). If you do not have a number, see How to get a TIN on page 3.")
  tokens = nlp(test_sentence)
  
  #this check should be last
  fill_verbs = set(['enter', 'fill', 'provide', 'list'])
  verbs = [t.orth_ for t in tokens if (t.pos_ == 'VERB' and str(t.orth_).lower() in fill_verbs)]
  
  actions = []
  for token in tokens:
    if token.pos_ == 'NOUN' and token.head.orth_ in verbs:
      actions.append(str(token.head.orth_) + " " + str(token.orth_))

  return str(form) + " " + str(actions)
