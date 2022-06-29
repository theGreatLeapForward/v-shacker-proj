import requests
from bs4 import BeautifulSoup
import csv
from googlesearch import search
import spacy
import numpy
from spacy.lang.en.examples import sentences
from pprint import pprint
from Questgen import main

if __name__ == '__main__':
    nlp = spacy.load("en_core_web_sm")
    # inp will be the search term
    urls = []
    inp = input('topic')
    keywords = input("keywords. Type 'N' to try funny")
    if keywords == 'N':
        keywords = inp.split()
    else:
        keywords = keywords.split()
    query = str(inp)
    for j in search(query, num_results=10):
        # print(j)
        urls.append(j)

        URL = j
        r = requests.get(URL)

        soup = BeautifulSoup(r.content, 'html5lib')
        print(soup.prettify())

        information = []  # a list to store relevant info
        for keyword in keywords:
            table = soup.find('div', attrs={'id': keyword})
            fullsentance = str(table)
            print(fullsentance)
            if fullsentance == 'None':
                print("No information found")
                continue

            for row in table.findAll('div'):
                sentance = {0: row.txt}
                sentences.append(sentance)

            filename = 'information.csv'
            with open(filename, 'w', newline='') as f:
                for sentance in sentences:
                    f.writerow()
                    text = (str(sentance))
                    doc = nlp(text)

                    # Analyze syntax
                    print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
                    print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])
                    # Find named entities, phrases and concepts
                    for entity in doc.ents:
                        print(entity.text, entity.label_)

                    qe = main.QGen()
                    payload = {
                        "input_text": str(sentance)}
                    output = qe.predict_mcq(payload)
                    pprint(output)

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

