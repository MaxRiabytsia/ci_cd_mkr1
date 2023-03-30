def read_data(file_name):
    with open(file_name, 'r') as f:
        data = [line.split(',') for line in f.read().splitlines()]
    return data


def sort_by_area(data):
    return sorted(data, key=lambda x: float(x[1]))


def sort_by_population(data):
    return sorted(data, key=lambda x: float(x[2]))


def main():
    data = read_data('data.txt')
    print(f'Sorted by area: {sort_by_area(data)}')
    print(f'Sorted by population: {sort_by_population(data)}')


if __name__ == '__main__':
    main()
