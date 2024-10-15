import requests
from bs4 import BeautifulSoup

ARTIST = "Cathie+Evans"
BASE_URL = "https://www.last.fm/music/{}"

BASE_URL_LYRICS = "https://genius.com/{}-lyrics"


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


def get_lyrics_for_song(song) -> list[str] | AttributeError:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
    response = requests.get(BASE_URL_LYRICS.format('-'.join(song.Artist.replace('\'', '').split() + song.Track.split()), headers=headers))
    if response.status_code != 200:
        print(f'haha {response.status_code}, {response.text}')
        return []

    soup = BeautifulSoup(response.content, "html.parser")
    soup = soup.find("div", {"data-lyrics-container": "true"})
    lyrics = []
    for elem in soup:
        if line := elem.next_element.text.strip():
            lyrics.append(line)

    try:
        return lyrics
    except AttributeError as err:
        return err
