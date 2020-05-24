## app/elephant_queries.py


import os
from dotenv import load_dotenv
from psycopg2.extras import DictCursor
import psycopg2


load_dotenv() ## reads the contents of the .env file and adds them to the environment

### this is what you gotta do to keep your credentials private
DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")
DB_HOST = os.getenv("DB_HOST", default="OOPS")

### Connect to ElephantSQL-hosted PostgreSQL
connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION", type(connection))



### A "cursor", a structure to iterate over db records to perform queries
cursor = connection.cursor(cursor_factory=DictCursor)
print("CURSOR", type(cursor))



### An example query
cursor.execute('SELECT * from test_table;')
### Note - nothing happened yet! We need to actually *fetch* from the cursor
##result = cursor.fetchone()
#print(type(result)) <class 'tuple'>
# result = cursor.fetchone()
#(1, 'A row name', None)


result = cursor.fetchall()
for row in result:
    print("----------")
    print(type(row))
    print(row)
