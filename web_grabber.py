import requests
from bs4 import BeautifulSoup
import csv
from googlesearch import search
import spacy


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

    filename = 'information.csv'
    with open(filename, 'w', newline='') as f:
        w = csv.DictWriter(f, ['theme', 'url', 'img', 'lines', 'author'])
        w.writeheader()
        for quote in quotes:
            w.writerow(quote)
            print(str(quote))

    # URL = "http://www.values.com/inspirational-quotes"
    # table = soup.find('div', attrs={'id': 'all_quotes'})
    #
    # for row in table.findAll('div',
    #                          attrs={'class': 'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
    #     quote = {}
    #     quote['theme'] = row.h5.text
    #     quote['url'] = row.a['href']
    #     quote['img'] = row.img['src']
    #     quote['lines'] = row.img['alt'].split(" #")[0]
    #     quote['author'] = row.img['alt'].split(" #")[1]
    #     quotes.append(quote)
    #
    # filename = 'inspirational_quotes.csv'
    # with open(filename, 'w', newline='') as f:
    #     w = csv.DictWriter(f, ['theme', 'url', 'img', 'lines', 'author'])
    #     w.writeheader()
    #     for quote in quotes:
    #         w.writerow(quote)
    #         print(str(quote))
import spacy

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")

# Process whole documents
text = ("When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously. “I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasn’t "
        "worth talking to,” said Thrun, in an interview with Recode earlier "
        "this week.")
doc = nlp(text)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doac.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])
# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)
