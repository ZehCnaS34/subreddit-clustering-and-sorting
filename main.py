import parser
import classify
import os.path
from glob import glob
import json
paths = glob('./data/*.csv')


def main():
    if not os.path.exists('relevantTerms.json'):
        relevant_terms = parser.get_subreddit_word_counts(paths, save_to_file=True)
    else:
        with open('relevantTerms.json') as data_file:
            relevant_terms = json.load(data_file)
        data_file.close()

    while True:
        print('Enter a request:')
        sentence = input()
        result = classify.classify(relevant_terms, sentence)
        print(result[:5])
        entities = parser.get_entities(sentence)
        print(entities)

if __name__ == '__main__':
    main()
