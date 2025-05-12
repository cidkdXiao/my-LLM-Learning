import langid
text = "Tudo bem?"
language = langid.classify(text)[0]
print(language)