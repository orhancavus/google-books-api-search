import requests
import sys
import json

# Usage from terminal : curl -X GET https://www.googleapis.com/books/v1/volumes\?q\=moby dick&maxResults=3•
endpoint = "https://www.googleapis.com/books/v1/volumes"

def search_books(query, maxResults):

    params = {"q": query, "maxResults": maxResults}
    response = requests.get(endpoint, params=params).json()

    books = []
    for book in response["items"]:
        volume = book["volumeInfo"]
        title = volume["title"]
        published = volume["publishedDate"]

        try:
            description = volume["description"]
        except:
            description = "description not found"

        records = {
            'title': title,
            'published': published,
            'description': description 
        }    

        books.append(records)
        
    return books

def write_result_to_file(books, filename):
    json_records = json.dumps(books)
    with open(filename, 'w') as f:
        f.write(json_records)    

if __name__ == "__main__":
    if len(sys.argv) == 1 : 
        print("\n Please provide book name to search ..")
        exit(0)

    parameter = sys.argv[1]

    print(f"Search for : {parameter}") 
    books = search_books(parameter,3)

    print("-" * 80)
    print(books)
    print("-" * 80)
    
    write_result_to_file(books, "books.json")

