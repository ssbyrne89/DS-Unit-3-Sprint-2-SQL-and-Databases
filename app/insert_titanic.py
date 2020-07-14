import os
import csv
import sqlite3
import psycopg2
import numpy as np
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine


# Load titanic from path

titanic = os.path.join(os.path.dirname(__file__), "..", "data", "titanic.csv")
df = pd.read_csv(titanic)

# Check df shape and null values

print(df.head(5))

# convert csv to sql

engine = create_engine('sqlite://', echo=False)
df.to_sql('titanic', con=engine)

load_dotenv()
DB_HOST = os.getenv("DB_HOST", default="OOPS")
DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")

connection = psycopg2.connect(dbname=DB_NAME,
                              user=DB_USER,
                              password=DB_PASSWORD,
                              host=DB_HOST)

cursor = connection.cursor()
print("CURSOR:", cursor)

# Create the table

create_titanic_table = """
CREATE TABLE titanic(
    id SERIAL PRIMARY KEY,
    survived INT,
    p_class INT,
    name VARCHAR(100),
    sex VARCHAR(100),
    age FLOAT,
    siblings_spouses_aboard INT,
    parents_children_aboard INT,
    fare FLOAT
);"""

cursor.execute(create_titanic_table)


engine.execute("""
UPDATE titanic SET name = REPLACE(name, "'", " ");
""")


passengers = engine.execute('SELECT * from titanic;').fetchall()

for passenger in passengers[1:]:
    insert_passenger = """
        INSERT INTO titanic
        VALUES""" + str(passenger) + ";"
    cursor.execute(insert_passenger)


connection.commit()

cursor.close()
