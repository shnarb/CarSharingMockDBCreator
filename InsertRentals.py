from InsertQueries import INSERT_QUERY_RENTALS
from Inserter import Inserter
import numpy as np
import random
import psycopg2
import pandas.io.sql as sqlio
import datetime
import math

adding_more = True

conn = psycopg2.connect(
    "host='{}' port={} dbname='{}' user={} password={}".format("localhost", 5432, "carsharing", "postgres", ""))
sql_moscow = "select id from locations WHERE locations.city='Moscow';"
moscow_ids = list(sqlio.read_sql_query(sql_moscow, conn).to_numpy().ravel())
sql_serp = "select id from locations WHERE locations.city='Serpukhov';"
serp_ids = list(sqlio.read_sql_query(sql_serp, conn).to_numpy().ravel())
sql_pet = "select id from locations WHERE locations.city='St. Petersburg';"
pet_ids = list(sqlio.read_sql_query(sql_pet, conn).to_numpy().ravel())
sql_clients = "select id from client"
client_ids = list(sqlio.read_sql_query(sql_clients, conn).to_numpy().ravel())
sql_vehicles = "select id from vehicle"
if adding_more:
    sql_end_times = "SELECT vehicle_id, MAX(time_end) from rentals GROUP BY vehicle_id"
    vehicle_ids = dict(list(sqlio.read_sql_query(sql_end_times, conn).to_numpy()))
else:
    vehicle_ids = list(sqlio.read_sql_query(sql_vehicles, conn).to_numpy().ravel())
    vehicle_ids = dict(zip(vehicle_ids, [datetime.datetime(2018, 1, 1, 0, 0) for _ in range(len(vehicle_ids))]))
conn = None


def gen_level_of_infraction():
    return np.random.choice([0, 1, 2, 3, 4, 5], p=[0.9, 0.05, 0.025, 0.015, 0.009, 0.001])


def generate_fine_amount(level_of_infraction):
    if level_of_infraction == 0:
        return 0
    elif level_of_infraction == 1:
        return random.random() * 100 + 100
    elif level_of_infraction == 2:
        return random.random() * 500 + 500
    elif level_of_infraction == 3:
        return random.random() * 2000 + 10000
    elif level_of_infraction == 4:
        return random.random() * 50000 + 100000
    elif level_of_infraction == 5:
        return random.random() * 1000000 + 1000000


def create_batch():
    rentals = []
    for vehicle_id in list(vehicle_ids.keys()):
        distance = np.random.poisson(8)
        duration = distance / (15 / 60)
        fuel_used = distance / 10 + random.random() * distance / 50
        level_of_infraction = gen_level_of_infraction()
        fine_amount = generate_fine_amount(level_of_infraction)
        client = random.choice(client_ids)
        start_time = vehicle_ids[vehicle_id] + datetime.timedelta(minutes=math.ceil(random.random() * 40))
        end_time = start_time + datetime.timedelta(minutes=math.ceil(duration))
        vehicle_ids[vehicle_id] = end_time
        city_id = random.choice([1, 2, 3])
        if city_id == 1:
            locations = random.sample(moscow_ids, 2)
        elif city_id == 2:
            locations = random.sample(serp_ids, 2)
        else:
            locations = random.sample(pet_ids, 2)
        rentals.append(
            [-1, duration, distance, fuel_used, int(level_of_infraction), fine_amount, int(client), int(vehicle_id),
             start_time.isoformat(), end_time.isoformat(), int(locations[0]), int(locations[1])])
    return rentals


def insert_rentals():
    inserter = Inserter()
    amount = 200 * 4 * 6
    for i in range(amount):
        inserter.insert_batch(create_batch(), INSERT_QUERY_RENTALS)
        if i % 200 == 0:
            print(f'{(i / amount) * 100}% done')


insert_rentals()