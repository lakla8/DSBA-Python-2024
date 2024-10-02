import pandas as pd
from parser import get_tags_by_artist
from tqdm import tqdm

COLUMNS_LIST = ['Danceability', 'Energy', 'Loudness', 'Speechiness','Acousticness', 'Instrumentalness', 'Liveness',
                'Valence', 'Tempo']


class Song:
    def __init__(self, line):
        self.Artist = line.Artist
        self.Track: str = line.Track
        self.Album = line.Album
        self.Likes = line.Likes
        self.Duration_ms = line.Duration_ms
        self.Musicality = line.loc[COLUMNS_LIST].values

    def __repr__(self):
        return f"{self.Artist}, {self.Track}, {self.Album}, {self.Likes}, {self.Duration_ms}, {self.Musicality}"


class Database:
    def __init__(self, path: str):
        self.db = dict()
        self.db_genres = dict()
        df = pd.read_csv(path, index_col=0)
        df.dropna(subset=COLUMNS_LIST, inplace=True)
        for column in COLUMNS_LIST:
            df.loc[:, column] = (df[column] - df[column].min()) / (df[column].max() - df[column].min())
        for i in range(df.shape[0]):
            line = df.iloc[i]
            self.add_song(line)

    @staticmethod
    def euclid_sum(vec1, vec2):
        sum_vec = 0
        for i in range(len(vec1)):
            sum_vec += (vec1[i] - vec2[i]) ** 2
        return sum_vec ** 0.5

    def add_song(self, line):
        self.db[line.Artist] = self.db.get(line.Artist, []) + [Song(line)]

    def add_genres(self, artist):
        self.db_genres[artist] = get_tags_by_artist(artist)

    def fetch_genres(self):
        for artist in tqdm(list(self.db.keys())[:20]):
            self.add_genres(artist)

    def search(self, request: str) -> Song:
        similar_songs = []
        for song in sum(self.db.values(), []):
            if song.Track.lower().find(request.lower()) != -1:
                similar_songs.append(song)
        for i, song in enumerate(similar_songs):
            print(f"{i + 1}, {song.Track} by {song.Artist}")
        user_choice = int(input("Which song do you meant?\n"))
        return similar_songs[user_choice - 1]

    def search_similar(self, target_song: Song, n: int = 5):
        similar_song = [] # deque([], maxlen=5)
        for i, song in enumerate(sum(self.db.values(), [])):
            if target_song == song:
                continue
            value = self.euclid_sum(target_song.Musicality, song.Musicality)
            similar_song.append((song, value))
            # if len(similar_song) == 0:
            #     similar_song.append((i, value))
            # else:
            #     while True:
            #         mid_elem = len(similar_song) // 2
            #         if value > similar_song[mid_elem][1]:
            #             mid_elem += (len(similar_song) - mid_elem) // 2
            #         elif value == similar_song[mid_elem][1]:
            #             similar_song.insert(mid_elem + 1, (i, value))
            #         else:
            #
        return sorted(similar_song, key=lambda x: x[1], reverse=False)[:n]

    def print(self):
        print(self.db)

    def max_songs(self):
        return max(self.db, key=lambda x: len(self.db[x]))
