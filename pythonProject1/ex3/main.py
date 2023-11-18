from ex3.car import Car
from ex3.statistics import Statistics
from ex3.test import test_avarage

def main():
    cars = [Car('Mercedes', 'C-Class', 2023, 'black'),
            Car('Mercedes', 'S-Class', 2023, 'black'),
            Car('Skoda', 'Oktavia', 2023, 'blue')]

    stats = Statistics(cars)
    print(stats.color_count('black'), stats.avarage_year('S-Class'))

test_avarage()
main()
