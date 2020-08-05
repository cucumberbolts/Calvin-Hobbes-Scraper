"""
This is a program for downloading Calvin and Hobbes
comics from gocomics.com.

authors: Lawrence Cheung and Julian Poon
"""

import os
import requests
from bs4 import BeautifulSoup

# See https://hackersandslackers.com/scraping-urls-with-beautifulsoup/ for inspiration

# Set the headers
HEADERS = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}


SEARCH_STRING = "Calvin and Hobbes Comic Strip"


def get_comic_url(month: int, day: int, year: int) -> str:
    """ Returns the url of the comic image """
    # The url of the comic strip
    url = f"https://www.gocomics.com/calvinandhobbes/{year}/{month}/{day}"

    # Request the page
    req = requests.get(url, HEADERS)
    soup = BeautifulSoup(req.content, 'html.parser')

    # Get all links with the lazyload img-fluid class
    links = soup.find_all(class_="lazyload img-fluid")

    # Search for the "Calvin and Hobbes Comic Strip" image
    for link in links:
        if SEARCH_STRING in link["alt"]:
            # Get the url of the image
            pic_url = link["src"]
            return pic_url

    print("Error: Could not find image!")


def save_comic(month: int, day: int, year: int, output_dir: str) -> None:
    """ Saves the comic from the given date """
    print(f"Saving comic from {month}/{day}/{year}!")

    # What file to save it as
    file_name = f"calvinhobbes_{year}_{month}_{day}.gif"

    # Get the url of the comic image
    pic_url = get_comic_url(month, day, year)

    # Request the image
    image = requests.get(pic_url, allow_redirects=True)

    # Save the file
    open(f"{output_dir}/{file_name}", 'wb').write(image.content)


def main() -> None:
    """ Main function """
    # Output directory for the comics
    output_dir = "CalvinAndHobbesComics"

    # Set the date to grab the comic
    year = 2020
    month = 7
    day = 2

    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

    print("Starting to download!")

    save_comic(month, day, year, output_dir)

    print("Finished downloading!")


if __name__ == "__main__":
    main()
