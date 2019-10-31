import random

import numpy as np

from InsertQueries import INSERT_QUERY_CLIENT
from Inserter import Inserter

passport_numbers = set()
drivers_license_numbers = set()
phone_nums = set()
phone_codes = [930, 900, 910, 912]

with open('./Names/MaleFirstNames') as MaleFirstNamesFile:
    MaleFirstNames = list(MaleFirstNamesFile)

with open('./Names/MaleMiddleNames') as MaleMiddleNamesFile:
    MaleMiddleNames = list(MaleMiddleNamesFile)

with open('./Names/MaleLastNames') as MaleLastNamesFile:
    MaleLastNames = list(MaleLastNamesFile)

with open('./Names/FemaleFirstNames') as FemaleFirstNamesFile:
    FemaleFirstNames = list(FemaleFirstNamesFile)

with open('./Names/FemaleMiddleNames') as FemaleMiddleNamesFile:
    FemaleMiddleNames = list(FemaleMiddleNamesFile)

with open('./Names/FemaleLastNames') as FemaleLastNamesFile:
    FemaleLastNames = list(FemaleLastNamesFile)


def generate_passport_number():
    p_num = np.random.randint(0, 9, 9)
    while p_num.tostring() in passport_numbers:
        p_num = np.random.randint(0, 9, 9)
    passport_numbers.add(p_num.tostring())
    return f'{"".join(map(str, p_num[:2]))} {"".join(map(str, p_num[2:]))}'


def generate_drivers_license_number():
    d_num = np.random.randint(0, 9, 10)
    while d_num.tostring() in drivers_license_numbers:
        d_num = np.random.randint(0, 9, 10)
    drivers_license_numbers.add(d_num.tostring())
    return f'{"".join(map(str, d_num[:2]))} {"".join(map(str, d_num[2:4]))} {"".join(map(str, d_num[4:]))}'


def generate_phone_number():
    phone_num = np.random.randint(0, 9, 7)
    while phone_num.tostring() in phone_nums:
        phone_num = np.random.randint(0, 9, 7)
    phone_nums.add(phone_num.tostring())
    return f'+7 ({np.random.choice(phone_codes)}) {"".join(map(str, phone_num[:3]))} {"".join(map(str, phone_num[3:5]))} {"".join(map(str, phone_num[5:]))}'


def generate_client_name(is_male):
    if is_male:
        return random.choice(MaleFirstNames), random.choice(MaleMiddleNames), random.choice(MaleLastNames)
    else:
        return random.choice(FemaleFirstNames), random.choice(FemaleMiddleNames), random.choice(FemaleLastNames)


def create_batch():
    clients = []
    for i in range(100):
        is_male = random.choice([True, False])
        if is_male:
            sex = 'Male'
        else:
            sex = 'Female'
        first_name, middle_name, last_name = generate_client_name(is_male)
        passport_number = generate_passport_number()
        drivers_license_number = generate_drivers_license_number()
        phone_number = generate_phone_number()
        clients.append([sex, first_name, middle_name, last_name, passport_number, drivers_license_number, phone_number])
    return clients


def insert_clients():
    inserter = Inserter()
    for i in range(10):
        inserter.insert_batch(create_batch(), INSERT_QUERY_CLIENT)


insert_clients()
