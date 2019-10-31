from InsertQueries import INSERT_QUERY_LOCATIONS
from Inserter import Inserter
import numpy as np
import random

address_list = set()
cities = ['Moscow', 'St. Petersburg', 'Serpukhov']
corpus_list = ['', '1', '2', '3']
with open('/home/karim/PycharmProjects/CarSharing/StreetNames') as StreetNamesFile:
    StreetNames = list(StreetNamesFile)


def create_batch():
    locations = []
    for i in range(100):
        city = random.choice(cities)
        street_name = random.choice(StreetNames)
        house_number = random.randint(1, 30)
        corpus = random.choice(corpus_list)
        str_hash = f'{city}{street_name}{house_number}{corpus}'
        while str_hash in address_list:
            city = np.random.choice(cities, [.40, .20, .20, .20])
            street_name = random.choice(StreetNames)
            house_number = random.randint(1, 30)
            corpus = np.random.choice(corpus_list, [.40, .20, .20, .20])
            str_hash = f'{city}{street_name}{house_number}{corpus}'
        locations.append([city, street_name, house_number, corpus])
    return locations


def insert_locations():
    inserter = Inserter()
    for i in range(450):
        inserter.insert_batch(create_batch(), INSERT_QUERY_LOCATIONS)


insert_locations()
