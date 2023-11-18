from ex3.statistics import Statistics
from ex3.car import Car

def test_avarage():
    cars = [Car('Mercedes', 'S-Class', 2023, 'black'),
             Car('Mercedes', 'S-Class', 2017, 'red'),
            Car('Skoda', 'Oktavia', 2014, 'blue')]
    stats = Statistics(cars)
    assert stats.avarage_year('S-Class') == 2020

test_avarage()
