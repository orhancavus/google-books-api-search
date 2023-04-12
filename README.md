# Google Books API Search Script

```text
Author : Orhan Chaushev
Date   : 12.04.2023
```

This Python script allows you to search for books using the Google Books API and retrieve information about them. You can specify a search query and a maximum number of results to return. The information is returned in JSON format and can be saved to a file for later use.

## Requirements

- Python 3
- requests library (`pip install requests`)

## Usage

1. Clone the repository or download the script file (`google_books_search.py`) to your computer.
2. Open a terminal or command prompt and navigate to the directory where the script is located.
3. Run the script using the following command:

    Replace `<search_query>` with your desired search query (enclosed in quotes if it contains spaces) and `<max_results>` with the maximum number of results you want to return (default is 10 if not specified).

4. The script will print the results to the console and save them to a file named `books.json` in the same directory as the script.

## Prettify json

```bash
jq '.' books.json

cat books.json | jq
```