import requests
from bs4 import BeautifulSoup
import csv
from googlesearch import search
import spacy
import numpy

nlp = spacy.load("en_core_web_sm")
#inp will be the search term
urls=[]
inp=input('topic')
keywords=input("keywords. Type 'N' to try funny")
if keywords=='N':
    keywords = inp.split()
else:
    keywords=keywords.split()
query = str(inp)
for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    #print(j)
    urls.append(j)

for item in j:

    URL = urls[item]
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    print(soup.prettify())

    information = []  # a list to store relevant info
    for keyword in keywords:
        table = soup.find('div', attrs={'id': keyword})
        fullsentance=str(table)
    for row in table.findAll('div'):
        sentance={}
        sentance[0] = row.txst
        sentances.append(sentance)

    filename = 'information.csv'
    with open(filename, 'w', newline='') as f:
        for sentance in sentances:
            w.writerow()
            text = (str(sentance))
            doc = nlp(text)

            # Analyze syntax
            print("Noun phrases:", [chunk.text for chunk in doac.noun_chunks])
            print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])
            # Find named entities, phrases and concepts
            for entity in doc.ents:
                print(entity.text, entity.label_)
    from pprint import pprint
    from Questgen import main

    qe = main.QGen()
    payload = {
        "input_text": str(sentance)}
    output = qg.predict_mcq(payload)
    pprint(output)
