import psycopg2


class Inserter:
    def __init__(self, user='postgres', password='', host='localhost', port=5432, database='carsharing'):
        try:
            self.connection = psycopg2.connect(
                user=user,
                password=password,
                host=host,
                port=port,
                database=database
            )
            self.cursor = self.connection.cursor()
            self.counter = 0
        except (Exception, psycopg2.Error) as error:
            print(f'Failed to connect {error}')

    def insert_batch(self, batch, insert_query):
        try:
            for record in batch:
                self.cursor.execute(insert_query, record)
                self.counter += self.cursor.rowcount
            self.connection.commit()
        except (Exception, psycopg2.Error) as error:
            if self.connection:
                print(f'Failed to insert batch {error}')

    def __del__(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print(f'PostgreSQL connection is closed, wrote {self.counter} rows')
