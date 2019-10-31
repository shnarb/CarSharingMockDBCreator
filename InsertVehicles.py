from InsertQueries import INSERT_QUERY_VEHICLE
from Inserter import Inserter
import numpy as np
import random

manufacturers_models = {'Honda': ['Accord', 'Amaze', 'Civic'],
                        'Audi': ['A1', 'A4', 'A7'],
                        'BMW': ['X2', 'X3', 'X5'],
                        'Volkswagen': ['Amarok', 'Ameo', 'Caddy', 'Golf', 'Fox']}

russian_alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т',
                    'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ы', 'Э', 'Ю', 'Я']

cost_per_minute = [8.5, 10, 11, 12.5]

car_numbers = set()


def generate_car_number():
    car_num = np.random.randint(0, 9, 6)
    first_letter = random.choice(russian_alphabet)
    last_letters = f'{random.choice(russian_alphabet)}{random.choice(russian_alphabet)}'
    str_car_num = f'{first_letter}{car_num[:3].tostring()}{car_num[3:]}{last_letters}'
    while str_car_num in car_numbers:
        car_num = np.random.randint(0, 9, 6)
        first_letter = random.choice(russian_alphabet)
        last_letters = random.choices(russian_alphabet, 2)
        str_car_num = f'{first_letter}{car_num[:3].tostring()}{car_num[3:]}{last_letters}'
    car_numbers.add(str_car_num)
    return f'{first_letter}{"".join(map(str, car_num[:3]))}{last_letters}{"".join(map(str, car_num[3:]))}'


def create_batch():
    vehicles = []
    for i in range(100):
        license_plate_number = generate_car_number()
        manufacturer = random.choice(list(manufacturers_models.keys()))
        model = random.choice(manufacturers_models[manufacturer])
        fuel_level = random.random() * 50
        capacity = 4
        cpm = random.choice(cost_per_minute)
        vehicles.append([license_plate_number, manufacturer, model, fuel_level, capacity, cpm])
    return vehicles


def insert_vehicles():
    inserter = Inserter()
    for i in range(2):
        inserter.insert_batch(create_batch(), INSERT_QUERY_VEHICLE)


insert_vehicles()
