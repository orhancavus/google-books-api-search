import requests

endpoint = "https://www.googleapis.com/books/v1/volumes"
query = "moby dick"

params = {"q": query, "maxResults": 3}
response = requests.get(endpoint, params=params).json()
#print(response)
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
