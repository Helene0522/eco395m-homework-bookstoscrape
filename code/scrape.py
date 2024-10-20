import os
import json
import csv

from scrape_pages import scrape_all_pages
from scrape_books import scrape_books


def scrape():
    """Scrape everything and return a list of books."""
    
    book_urls = scrape_all_pages()

    
    books = scrape_books(book_urls)

    return books


def write_books_to_csv(books, path):
    """Writes the list of books to a CSV file."""
    
    fieldnames = ["upc", "title", "category", "description", "price_gbp", "stock"]

    
    with open(path, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        
        writer.writeheader()

        
        for book in books:
            writer.writerow(book)


def write_books_to_jsonl(books, path):
    """Writes the list of books to a JSONL file."""
    
    with open(path, mode="w", encoding="utf-8") as jsonlfile:
        for book in books:
            jsonlfile.write(json.dumps(book) + "\n")


if __name__ == "__main__":

    BASE_DIR = "artifacts"
    CSV_PATH = os.path.join(BASE_DIR, "results.csv")
    JSONL_PATH = os.path.join(BASE_DIR, "results.jsonl")

    os.makedirs(BASE_DIR, exist_ok=True)

    
    books = scrape()

    
    write_books_to_csv(books, CSV_PATH)
    write_books_to_jsonl(books, JSONL_PATH)
