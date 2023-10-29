class CarInfo:
    def __init__(self, car_info):
        self.car_info = car_info

    def car_information(self):
        return self.car_info


class CarFamilies:
    cars = {}

    def __new__(cls, car_id):
        try:
            car_obj_id = cls.cars[car_id]
        except KeyError:
            car_obj_id = object.__new__(cls)
            cls.cars[car_id] = car_obj_id
        return car_obj_id

    @staticmethod
    def car_information(car_information):
        return CarInfo(car_information).car_information()


if __name__ == '__main__':
    cars = [(1, 'AUDI'), (2, 'TATA'), (3, 'ASHOK LELAND'), (2, 'TATA MOTORS')]
    for cars_object in cars:
        car = CarFamilies(cars_object[0])
        print('car_id: ', id(car))
        print('car_info: ', car.car_information(cars_object[1]))
