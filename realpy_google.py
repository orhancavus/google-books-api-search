"""
Module Name: google_books_api
Purpose: Demonstrates how to use the Google Books API to search for books.
Author:  Orhan CHAUSHEV
Usage: python google_books_api.py
        (or) 
       import google_books_api
       google_books_api.search_books()
Usage from terminal : curl -X GET https://www.googleapis.com/books/v1/volumes\?q\=moby dick&maxResults=3•
Dependencies: requests
Input: None
Output: Prints the title, published date, and description (if available) of the top 3 search results for the query "moby dick".
"""

import requests

endpoint = "https://www.googleapis.com/books/v1/volumes"
query = "moby dick"

params = {"q": query, "maxResults": 3}
response = requests.get(endpoint, params=params).json()

print(response)

for book in response["items"]:
    volume = book["volumeInfo"]
    title = volume["title"]
    published = volume["publishedDate"]
    print("-"*80)

    try:
        description = volume["description"]
    except:
        description = "description not found"
    print(f"{title} ({published}) | {description}")
