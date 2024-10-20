from common import get_soup

def scrape_page(num):
    """Takes a page number and returns a list of links to the books that are on the page."""
    url = f"http://books.toscrape.com/catalogue/page-{num}.html"
    soup = get_soup(url)
    
    # 查找页面中书籍的链接，每个书籍在 <article class="product_pod"> 标签中
    book_links = []
    articles = soup.find_all("article", class_="product_pod")
    
    for article in articles:
        # 获取书籍页面的相对链接
        link = article.find("a")["href"]
        # 拼接成完整的书籍链接
        full_link = "http://books.toscrape.com/catalogue/" + link
        book_links.append(full_link)
    
    return book_links

def scrape_all_pages():
    """Scrapes all pages, returning a list of book links."""
    all_book_links = []
    page_num = 1

    while True:
        book_links = scrape_page(page_num)
        if not book_links:  # 当返回空列表时，说明没有更多页面
            break
        all_book_links.extend(book_links)
        page_num += 1
    
    return all_book_links

if __name__ == "__main__":
    # code for testing

    # test scrape_page

    page_3_actual_book_urls = [
        "http://books.toscrape.com/catalogue/slow-states-of-collapse-poems_960/index.html",
        "http://books.toscrape.com/catalogue/reasons-to-stay-alive_959/index.html",
        "http://books.toscrape.com/catalogue/private-paris-private-10_958/index.html",
        "http://books.toscrape.com/catalogue/higherselfie-wake-up-your-life-free-your-soul-find-your-tribe_957/index.html",
        "http://books.toscrape.com/catalogue/without-borders-wanderlove-1_956/index.html",
        "http://books.toscrape.com/catalogue/when-we-collided_955/index.html",
        "http://books.toscrape.com/catalogue/we-love-you-charlie-freeman_954/index.html",
        "http://books.toscrape.com/catalogue/untitled-collection-sabbath-poems-2014_953/index.html",
        "http://books.toscrape.com/catalogue/unseen-city-the-majesty-of-pigeons-the-discreet-charm-of-snails-other-wonders-of-the-urban-wilderness_952/index.html",
        "http://books.toscrape.com/catalogue/unicorn-tracks_951/index.html",
        "http://books.toscrape.com/catalogue/unbound-how-eight-technologies-made-us-human-transformed-society-and-brought-our-world-to-the-brink_950/index.html",
        "http://books.toscrape.com/catalogue/tsubasa-world-chronicle-2-tsubasa-world-chronicle-2_949/index.html",
        "http://books.toscrape.com/catalogue/throwing-rocks-at-the-google-bus-how-growth-became-the-enemy-of-prosperity_948/index.html",
        "http://books.toscrape.com/catalogue/this-one-summer_947/index.html",
        "http://books.toscrape.com/catalogue/thirst_946/index.html",
        "http://books.toscrape.com/catalogue/the-torch-is-passed-a-harding-family-story_945/index.html",
        "http://books.toscrape.com/catalogue/the-secret-of-dreadwillow-carse_944/index.html",
        "http://books.toscrape.com/catalogue/the-pioneer-woman-cooks-dinnertime-comfort-classics-freezer-food-16-minute-meals-and-other-delicious-ways-to-solve-supper_943/index.html",
        "http://books.toscrape.com/catalogue/the-past-never-ends_942/index.html",
        "http://books.toscrape.com/catalogue/the-natural-history-of-us-the-fine-art-of-pretending-2_941/index.html",
    ]

    page_3_book_urls = scrape_page(3)

    assert set(page_3_book_urls) == set(page_3_actual_book_urls)
