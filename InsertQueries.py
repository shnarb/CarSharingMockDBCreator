INSERT_QUERY_CLIENT = 'INSERT INTO client ' \
                      '(sex, name, middle_name, last_name, passport_number, drivers_license_number, phone_number) ' \
                      'VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING'

INSERT_QUERY_LOCATIONS = 'INSERT INTO locations ' \
                         '(city, street_name, house_number, corpus) ' \
                         'VALUES (%s, %s, %s, %s) ON CONFLICT DO NOTHING'

INSERT_QUERY_RENTALS = 'INSERT INTO rentals ' \
                       '(price, duration, distance, fuel_used, level_of_infraction, fine_amount, client_id, vehicle_id,\
                        time_start, time_end, location_start, location_end) ' \
                       'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, TIMESTAMP %s, TIMESTAMP %s, %s, %s) ON CONFLICT DO NOTHING'

INSERT_QUERY_TIMES = 'INSERT INTO times ' \
                     '(time) ' \
                     'VALUES (TO_TIMESTAMP(201901012301, YYYYMMDDHH24MI)) ON CONFLICT DO NOTHING'

INSERT_QUERY_VEHICLE = 'INSERT INTO vehicle ' \
                       '(license_plate_number, manufacturer, model, fuel_level, capacity, cost_per_minute) ' \
                       'VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING'
