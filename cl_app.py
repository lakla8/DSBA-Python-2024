import argparse
import csv
import pandas as pd
from collections import deque

LAST_INDEX = 19
ARTISTS_AMOUNT = 5
COLUMN = 8
COLUMNS_LIST = ['Danceability', 'Energy', 'Loudness', 'Speechiness','Acousticness', 'Instrumentalness', 'Liveness',
                'Valence', 'Tempo']
parser = argparse.ArgumentParser()


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
            similar_song.append((i, value))
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
        return sorted(similar_song, key=lambda x: x[1], reverse=True)[:n]

    def print(self):
        print(self.db)

    def max_songs(self):
        return max(self.db, key=lambda x: len(self.db[x]))


def reading_data(path: str = "data/Spotify_Youtube.csv"):
    """returns data from given csv(hand version)"""
    big_data = []
    with open(path) as f:
        header = [i for i in f.readline().strip().split(',')]
        while True:
            line = f.readline()
            if not line:
                break
            if line.split(',')[0].isnumeric():
                temp_data = [i for i in line.strip().split(',')][:LAST_INDEX]
                if len(temp_data) >= LAST_INDEX:
                    big_data.append(temp_data)

    return header, big_data


def reading_data_2(path: str = "data/Spotify_Youtube.csv"):
    """returns data from given csv(csv lib version)"""
    data = []
    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    header = data[0]
    return header, data[1:]


def size(data: list) -> [int, int]:
    """receive size of dataset NxM"""
    return len(data), len(data[0])


def get_max_min(data: list[list[str]], column: int) -> [float, float]:
    """returns max and minimum element from specific column of dataset
    (exceptions included)
    """
    if 0 > column > len(data):
        raise IndexError('out of bounds')
    temp_data = [float(row[column]) for row in data if row[column].replace('.', '', 1).isdigit()]
    if len(temp_data) > 0.8*len(data):
        return max(temp_data), min(temp_data)
    raise TypeError('wrong column(int column expected)')


def get_top_n_artists(data: list[list[str]], n: int = 5) -> [str]:
    """returns top n popular artists(aka with most amount of songs)"""
    artists_songs = dict()
    for row in data:
        artists_songs[row[1]] = artists_songs.get(row[1], 0)+1
    return sorted(artists_songs.items(), key=lambda x: x[1], reverse=True)[:n]


def parser_config(arg_parser: argparse.ArgumentParser()):
    """parser settings configuration"""
    arg_parser.add_argument('-c', "--column", type=int, help='specify column for max-min method')
    arg_parser.add_argument('-n', "--number", type=int, help='top n artists from data')


def arguments():
    """read arguments from console or putting saved constants"""
    args = parser.parse_args()
    return args.column or COLUMN, args.number or ARTISTS_AMOUNT


def main():
    db = Database("data/Spotify_Youtube.csv")
    print(db.search_similar(db.search('aaa'), 5))
    parser_config(parser)



if __name__ == "__main__":
    main()



