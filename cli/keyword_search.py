import json
import string

def file_search(query): 
    with open("data/movies.json", "r") as file:
        data = json.load(file)
    movie_list = []
    for movie in data["movies"]:
        processed_query = process_text(query)
        processed_title = process_text(movie["title"])
        if processed_query in processed_title:
            movie_list.append(movie)
    movie_list = movie_list[:5]
    return movie_list

def process_text(text: str):
    text = text.lower()
    translator = str.maketrans('','', string.punctuation)
    text = text.translate(translator)
    return text
