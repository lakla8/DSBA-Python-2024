LAST_INDEX = 19


def reading_data(path: str = "data/Spotify_Youtube.csv"):
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


def main():
    header, data = reading_data()
    return


if __name__ == "__main__":
    main()



