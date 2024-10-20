import os
import json
import csv

from scrape_pages import scrape_all_pages
from scrape_books import scrape_books


def scrape():
    """Scrape everything and return a list of books."""
    # Step 1: Scrape all book URLs
    book_urls = scrape_all_pages()

    # Step 2: Scrape all book details from URLs
    books = scrape_books(book_urls)

    return books


def write_books_to_csv(books, path):
    """Writes the list of books to a CSV file."""
    # Define the CSV header
    fieldnames = ["upc", "title", "category", "description", "price_gbp", "stock"]

    # Write the books data to CSV
    with open(path, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header
        writer.writeheader()

        # Write book data
        for book in books:
            writer.writerow(book)


def write_books_to_jsonl(books, path):
    """Writes the list of books to a JSONL file."""
    # Write the books data to JSONL
    with open(path, mode="w", encoding="utf-8") as jsonlfile:
        for book in books:
            jsonlfile.write(json.dumps(book) + "\n")


if __name__ == "__main__":

    BASE_DIR = "artifacts"
    CSV_PATH = os.path.join(BASE_DIR, "results.csv")
    JSONL_PATH = os.path.join(BASE_DIR, "results.jsonl")

    os.makedirs(BASE_DIR, exist_ok=True)

    # Step 3: Scrape all books
    books = scrape()

    # Step 4: Write books to CSV and JSONL
    write_books_to_csv(books, CSV_PATH)
    write_books_to_jsonl(books, JSONL_PATH)
