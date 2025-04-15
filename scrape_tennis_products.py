import requests
from bs4 import BeautifulSoup

# URL of the product listing page
url = 'https://www.tennis-point.co.uk/tennis-rackets/'

# Set headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Send a GET request to the product page
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all product containers
    product_containers = soup.find_all('div', class_='col-12 col-md-6 item-list-element')

    # Loop through each product container and extract title and price
    for product in product_containers:
        print("1", product)
        # Extract product title
        title = product.find('div', class_='link').text.strip()
        print("1", title)

        # Extract product price
        price = product.find('span', class_='price-item price-item--regular').text.strip()

        # Print the product information
        print(f'Product Title: {title}')
        print(f'Product Price: {price}')
        print('---')
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)
