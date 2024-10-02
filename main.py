from database import Database
import random
from parser import get_lyrics_for_song


def main(db):
    db = Database("data/Spotify_Youtube.csv")
    # db.fetch_genres()
    # print(db.db_genres)
    artist_id: str = random.choice(list(db.db.keys()))
    # print(db.search_similar(db.search('aaa'), 5))
    # print(get_lyrics_for_song(db.db[artist_id][random.randrange(0, len(db.db[artist_id]))]))
    print(*db.db[artist_id][0].get_lyrics_for_song(), sep='\n')


if __name__ == "__main__":
    main()
