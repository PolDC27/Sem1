class Statistics:
    def __init__(self, carlist):
        self.carlist = carlist

    def color_count(self,color):
        counter = 0
        for car in self.carlist:
            if car.color == color:
                counter += 1
        return counter

    def avarage_year(self, model):
        sum = 0
        count = 0
        for car in self.carlist:
            if car.model == model:
                sum += car.year
                count += 1
        return sum // count


