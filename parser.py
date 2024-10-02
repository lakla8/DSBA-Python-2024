import requests
from bs4 import BeautifulSoup

ARTIST = "Cathie+Evans"
BASE_URL = "https://www.last.fm/music/{}"


def get_tags_by_artist(artist: str) -> list[str]:
    response = requests.get(BASE_URL.format(artist))
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.content, "html.parser")
    soup = soup.find("section", {"class": "catalogue-tags"})
    try:
        return [tag.text.strip() for tag in soup.find_all("li")]
    except AttributeError as err:
        return []

