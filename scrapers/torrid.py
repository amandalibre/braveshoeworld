import requests
from bs4 import BeautifulSoup

shoe_urls = []

def get_shoe_urls(url, shoe_list):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    shoes = soup.find(id="search-result-items")
    for shoe in shoes.find_all('li'):
        shoe_list.append(shoe.find('a')['href'])
    try:
        get_shoe_links(soup.find('a', class_='page-next')['href'], shoe_urls)
    except KeyError:
        print("last page")

def get_shoe_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    sizes = soup.find('li', class_='size-variation').find('ul', class_='swatches')
    for size_aval in sizes.find_all('li')[:-1]:
        print(size_aval['class'])
        if "unselectable" in (size_aval['class']):
            continue
        else:
            size = size_aval.find('span', class_='color-value')
            print(size.text)

get_shoe_urls("https://www.torrid.com/shoes-accessories/shoes/", shoe_urls)

for url in shoe_urls:
    get_shoe_data(url)