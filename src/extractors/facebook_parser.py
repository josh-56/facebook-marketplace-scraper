thonimport requests
from bs4 import BeautifulSoup

def parse_facebook_marketplace(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    products = []
    for listing in soup.find_all('div', class_='marketplace-item'):
        product = {
            'url': listing.find('a')['href'],
            'title': listing.find('span', class_='title').text,
            'initial_price': listing.find('span', class_='initial-price').text,
            'final_price': listing.find('span', class_='final-price').text,
            'currency': listing.find('span', class_='currency').text,
            'product_id': listing['data-id'],
            'breadcrumbs': [{'breadcrumbs_name': category.text, 'breadcrumbs_url': category['href']} for category in listing.find_all('a', class_='breadcrumb')],
            'condition': listing.find('span', class_='condition').text,
            'description': listing.find('span', class_='description').text,
            'location': listing.find('span', class_='location').text,
            'country_code': 'us',  # Placeholder for country code
            'root_category': 'General',  # Placeholder for category
            'images': [img['src'] for img in listing.find_all('img', class_='product-image')],
            'seller_description': listing.find('span', class_='seller-description').text if listing.find('span', class_='seller-description') else '',
            'color': listing.find('span', class_='color').text if listing.find('span', class_='color') else None,
            'brand': listing.find('span', class_='brand').text if listing.find('span', class_='brand') else None,
            'videos': [video['src'] for video in listing.find_all('video')]
        }
        products.append(product)

    return products