def read_data():
    with open('data.txt', 'r') as f:
        data = [line.split(',') for line in f.read().splitlines()]
    return data


def main():
    data = read_data()


if __name__ == '__main__':
    main()
