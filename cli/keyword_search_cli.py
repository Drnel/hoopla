#!/usr/bin/env python3

import argparse
import json


def file_search(query): 
    with open("data/movies.json", "r") as file:
        data = json.load(file)
    movie_list = []
    for movie in data["movies"]:
        if query in movie["title"]:
            movie_list.append(movie)
    movie_list = movie_list[:5]
    for i in range(len(movie_list)):
        print(f"{i + 1}. {movie_list[i]["title"]}")

def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    match args.command:
        case "search":
            print(f"Searching for: {args.query}")
            file_search(args.query)
            pass
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
