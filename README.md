# Google Books API Search

This program demonstrates how to use the Google Books API to search for books and retrieve information about them. It is written in Python and uses the `requests` library to make HTTP requests to the API.

## Getting Started

1. Clone this repository to your local machine using `git clone https://github.com/orhancavus/google-books-api-search.git`.
2. Install the `requests` library by running `pip install requests`.
3. Run the program by executing `python search.py` in your terminal.

## Usage

The program prompts the user to enter a search query. It then makes a request to the Google Books API with the query as a parameter and retrieves information about the top 3 results. The information retrieved includes the book title, published date, and description (if available).

## Dependencies

The program requires the `requests` library to be installed. You can install it using `pip install requests`.

## Prettify Json with jq

```bash
cat books.json | jq

jq '.' books.json
```