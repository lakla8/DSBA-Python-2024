from database import Database


def main():
    db = Database("data/Spotify_Youtube.csv")
    db.fetch_genres()
    print(db.db_genres)
    # print(db.search_similar(db.search('aaa'), 5))


if __name__ == "__main__":
    main()
