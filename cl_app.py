import argparse
import csv
from database import Database


LAST_INDEX = 19
ARTISTS_AMOUNT = 5
COLUMN = 8
COLUMNS_LIST = ['Danceability', 'Energy', 'Loudness', 'Speechiness','Acousticness', 'Instrumentalness', 'Liveness',
                'Valence', 'Tempo']
parser = argparse.ArgumentParser()


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



