from common import get_soup


def extract_price(price_str):
    """Extracts the price from the string in the product description as a float."""
    # 移除可能的特殊字符并提取数字部分
    price = price_str.replace("Â", "").replace("£", "").strip()
    return float(price)


def extract_stock(stock_str):
    """Extracts the count from the string in the product description as an int."""
    stock = stock_str.split("(")[-1].split()[0]  # 提取数字部分
    return int(stock)


def get_category(soup):
    """Extracts the category from the BeautifulSoup instance representing a book page as a string."""
    breadcrumb_tag = soup.find_all("ul", class_="breadcrumb")[0]
    a_tags = breadcrumb_tag.find_all("a")
    # 第三个 <a> 标签是分类
    return a_tags[2].text.strip()


def get_title(soup):
    """Extracts the title from the BeautifulSoup instance representing a book page as a string."""
    title = soup.find("h1").text.strip()
    return title


def get_description(soup):
    """Extracts the description from the BeautifulSoup instance representing a book page as a string."""
    description_tag = soup.find("meta", attrs={"name": "description"})
    if description_tag and description_tag.get("content", "").strip():
        return description_tag["content"].strip()
    return None  # 没有描述时返回 None



def get_product_information(soup):
    """Extracts the product information from the BeautifulSoup instance representing a book page as a dict."""
    product_info = {}
    table = soup.find("table", class_="table table-striped")
    rows = table.find_all("tr")
    
    for row in rows:
        header = row.find("th").text.strip()
        value = row.find("td").text.strip()
        
        if header == "UPC":
            product_info["upc"] = value
        elif header == "Price (incl. tax)":
            product_info["price_gbp"] = extract_price(value)
        elif header == "Availability":
            product_info["stock"] = extract_stock(value)
    
    return product_info


def scrape_book(book_url):
    """Extracts all information from a book page and returns a dict."""
    soup = get_soup(book_url)
    
    book_data = {
        "title": get_title(soup),
        "category": get_category(soup),
        "description": get_description(soup),
    }
    product_info = get_product_information(soup)
    book_data.update(product_info)  # 合并 product_information 数据
    
    return book_data


def scrape_books(book_urls):
    """Extracts all information from a list of book pages and returns a list of dicts."""
    books_data = []
    
    for url in book_urls:
        book_data = scrape_book(url)
        books_data.append(book_data)
    
    return books_data


if __name__ == "__main__":
    # code for testing

    book_url = "http://books.toscrape.com/catalogue/the-secret-of-dreadwillow-carse_944/index.html"
    book_url_no_description = "http://books.toscrape.com/catalogue/the-bridge-to-consciousness-im-writing-the-bridge-between-science-and-our-old-and-new-beliefs_840/index.html"

    soup = get_soup(book_url)
    soup_no_description = get_soup(book_url_no_description)

    # test extract_price
    assert extract_price("£56.13") == 56.13

    # test extract_stock
    assert extract_stock("In stock (16 available)") == 16

    # test get_category
    assert get_category(soup) == "Childrens"

    # test get_title
    assert get_title(soup) == "The Secret of Dreadwillow Carse"

    # test get_description
    assert get_description(soup) is not None
    assert get_description(soup_no_description) is None

    # test get_product_information
    product_information = get_product_information(soup)

    assert set(product_information.keys()) == {"upc", "price_gbp", "stock"}
    assert product_information == {
        "upc": "b5ea0b5dabed25a8",
        "price_gbp": 56.13,
        "stock": 16,
    }

    # test scrape_book
    book = scrape_book(book_url)
    book_no_description = scrape_book(book_url_no_description)

    expected_keys = {"title", "category", "description", "upc", "price_gbp", "stock"}

    assert set(book.keys()) == expected_keys
    assert set(book_no_description.keys()) == expected_keys
