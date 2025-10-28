import json
import string
from nltk.stem import PorterStemmer

def file_search(query): 
    with open("data/movies.json", "r") as file:
        data = json.load(file)
    movie_list = []
    for movie in data["movies"]:
        query_tokens = process_text(query)
        title_tokens = process_text(movie["title"])
        if any(query_token in title_token for query_token in query_tokens for title_token in title_tokens):
            movie_list.append(movie)
    movie_list = movie_list[:5]
    return movie_list

def process_text(text: str):
    text = text.lower()
    translator = str.maketrans('','', string.punctuation)
    text = text.translate(translator)
    tokens = text.split()
    with open("data/stopwords.txt", "r") as file:
        content = file.read()
        stop_words = content.splitlines()
    filtered = [word for word in tokens if word not in stop_words]
    stemmer = PorterStemmer()
    stemmed = [stemmer.stem(word) for word in filtered]
    return stemmed
