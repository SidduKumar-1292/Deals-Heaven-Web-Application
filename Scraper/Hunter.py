import aiohttp
import asyncio
from bs4 import BeautifulSoup
import csv
import os
import time
from urllib.parse import urljoin

BASE_URL = "https://dealsheaven.in"
STORES = [
    "Flipkart", "Amazon", "Paytm", "Foodpanda", "Freecharge",
    "paytmmall", "All Stores"
]
CATEGORIES = [
    "All Categories", "Beauty And Personal Care", "Electronics", "Grocery",
    "Recharge"
]
DEALS = ["Hot Deals Online", "Popular Deals"]
CSV_FILENAME = "scraped_deals.csv"

async def fetch_page(session, url):
    """Fetch a single page asynchronously."""
    try:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.text()
            else:
                print(f"Failed to fetch {url}. HTTP Status: {response.status}")
                return None
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

async def scrape_page(session, url, store_name, category_name):
    """Scrape a single page of deals."""
    html_content = await fetch_page(session, url)
    if not html_content:
        return []

    soup = BeautifulSoup(html_content, "html.parser")
    all_items = soup.find_all("div", class_="product-item-detail")

    if not all_items:
        print(f"No products found on {url}.")
        return []

    products = []
    for item in all_items:
        product = {
            "Store": store_name,
            "Category": category_name,
            "Title": "N/A",
            "Image": "N/A",
            "Price": "N/A",
            "Discount": "N/A",
            "Special Price": "N/A",
            "Link": "N/A",
        }

        discount = item.find("div", class_="discount")
        product["Discount"] = discount.text.strip() if discount else "N/A"

        link = item.find("a", href=True)
        product["Link"] = urljoin(BASE_URL, link["href"]) if link else "N/A"

        image = item.find("img", src=True)
        if image and 'data-src' in image.attrs:
            product["Image"] = urljoin(BASE_URL, image["data-src"])
        elif image and 'src' in image.attrs:
            product["Image"] = urljoin(BASE_URL, image["src"])
        else:
            product["Image"] = "https://via.placeholder.com/150"

        details_inner = item.find("div", class_="deatls-inner")

        title = details_inner.find("h3", title=True) if details_inner else None
        product["Title"] = title["title"].strip() if title else "N/A"

        price = details_inner.find("p", class_="price") if details_inner else None
        product["Price"] = price.text.strip() if price else "N/A"

        special_price = details_inner.find("p", class_="spacail-price") if details_inner else None
        product["Special Price"] = special_price.text.strip() if special_price else "N/A"

        products.append(product)
    return products

async def scrape_deals_for_category(session, store_name, category_name):
    """Scrape all pages for a store and category."""
    page = 1
    all_products = []

    while True:
        if category_name == "All Categories":
            url = f"{BASE_URL}/store/{store_name.lower()}?page={page}"
        else:
            formatted_category = category_name.lower().replace(" ", "-")
            url = f"{BASE_URL}/category/{formatted_category}?store={store_name.lower()}&page={page}"

        print(f"Scraping {url} for {store_name} in {category_name}...")
        products = await scrape_page(session, url, store_name, category_name)
        if not products:
            break

        all_products.extend(products)
        page += 1

    return all_products

async def scrape_all():
    """Scrape all stores, categories, and deals."""
    async with aiohttp.ClientSession() as session:
        all_products = []

        tasks = []
        for store in STORES:
            for category in CATEGORIES:
                tasks.append(scrape_deals_for_category(session, store, category))

        results = await asyncio.gather(*tasks)
        for result in results:
            all_products.extend(result)

        # Scrape deals tabs (Hot Deals Online & Popular Deals)
        for deal_tab in DEALS:
            deal_url = f"{BASE_URL}/{deal_tab.lower().replace(' ', '-')}"
            print(f"Scraping {deal_tab}...")
            products = await scrape_page(session, deal_url, "Deals Tab", deal_tab)
            all_products.extend(products)

        return all_products

def save_to_csv(products):
    """Save scraped products to a CSV file."""
    file_exists = os.path.isfile(CSV_FILENAME)
    with open(CSV_FILENAME, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Store", "Category", "Title", "Image", "Price", "Discount", "Special Price", "Link"])

        for product in products:
            writer.writerow(product.values())

if __name__ == "__main__":
    start_time = time.time()
    products = asyncio.run(scrape_all())
    save_to_csv(products)
    print(f"Scraping completed in {time.time() - start_time:.2f} seconds.")
