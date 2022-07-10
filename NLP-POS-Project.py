import spacy
import re
import glob

nlp = spacy.load("en_core_web_sm")

path = "/content/big.txt"
for file in glob.glob(path):
    with open(file, encoding='utf-8', errors='ignore') as bigFile:
        text = bigFile.read()
        pattern = '[a-zA-Z]+'
        lines = re.findall(pattern,text, flags=re.IGNORECASE)
        for line in lines:
            line = nlp(line)
            for word in line:
              if spacy.explain(word.pos_)=='noun' or spacy.explain(word.pos_)=='adverb':
                  print(word,":",spacy.explain(word.pos_))
