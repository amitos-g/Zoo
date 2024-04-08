import psycopg2
from psycopg2.errors import UniqueViolation
import atexit
from animals import AnimalRequest, AnimalResponse


class PostgresClient:
    def __init__(self, HOST, PORT, PASSWORD):

        self.connection = psycopg2.connect(dbname='postgres', user='postgres',
                                      host=HOST, port=PORT,
                                      password=PASSWORD)
        self.db_pointer = self.connection.cursor()

        ### SETUP ###
        self.db_pointer.execute("""CREATE TABLE IF NOT EXISTS animal(
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            type VARCHAR(255),
            color VARCHAR(255),
            size REAL,
            gender CHAR
        )
        """)
        self.connection.commit()
    def insert(self, animal : AnimalRequest):
        sql = f"""INSERT INTO animal (name, type, color, size, gender) VALUES
                (%s, %s, %s, %s, %s);"""

        # Tuple containing values to be inserted
        values = (animal.name, animal.__class__.__name__, animal.color, animal.size, animal.gender[0])
        # Execute the query with parameterized values
        try:
            self.db_pointer.execute(sql, values)
            self.db_pointer.execute("SELECT LASTVAL()")
            inserted_id = self.db_pointer.fetchone()[0]
            self.connection.commit()
            return inserted_id

        except UniqueViolation:
            self.connection.rollback()
            return -1
    def get_all(self):
        sql = f"""SELECT id, name, type, color, size, gender FROM animal"""
        try:
            res = []
            self.db_pointer.execute(sql)
            rows = self.db_pointer.fetchall()
            for row in rows:
                animal = AnimalResponse(row)
                res.append(animal)
            return res
        except Exception:
            self.connection.rollback()
            return -1
    def get_air(self):
        sql = f"""SELECT id, name, type, color, size, gender FROM animal WHERE type IN ('Crow', 'Parrow', 'Pigeon')"""
        try:
            res = []
            self.db_pointer.execute(sql)
            rows = self.db_pointer.fetchall()
            for row in rows:
                animal = AnimalResponse(row)
                res.append(animal)
            return res
        except Exception:
            self.connection.rollback()
            return -1
    def get_sea(self):
        sql = f"""SELECT id, name, type, color, size, gender FROM animal WHERE type IN ('Whale', 'Shark', 'Dolphin')"""
        try:
            res = []
            self.db_pointer.execute(sql)
            rows = self.db_pointer.fetchall()
            for row in rows:
                animal = AnimalResponse(row)
                res.append(animal)
            return res
        except Exception:
            self.connection.rollback()
            return -1
    def get_land(self):
        sql = f"""SELECT id, name, type, color, size, gender FROM animal WHERE type IN ('Lion', 'Monkey', 'Tiger')"""
        try:
            res = []
            self.db_pointer.execute(sql)
            rows = self.db_pointer.fetchall()
            for row in rows:
                animal = AnimalResponse(row)
                res.append(animal)
            return res
        except Exception:
            self.connection.rollback()
            return -1
    def close_db(self):
        self.db_pointer.close()
        self.connection.close()

def setup(host, port, password):
    db_client = PostgresClient(host, port, password)
    atexit.register(db_client.close_db)
    return db_client

