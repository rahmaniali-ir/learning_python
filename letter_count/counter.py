def count_chars(sentence):
  chars = {}

  for c in sentence.lower():
    if c in chars:
      chars[c] += 1
    else:
      chars[c] = 1
  
  return chars