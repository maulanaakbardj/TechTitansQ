import psycopg2
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
import json
import pyodbc

with open('user_address.json') as data_file:    
    d = json.load(data_file)
    
conn=psycopg2.connect(
        host = "localhost",
        user = "postgres",
        password = "secret123",
        database = "shipping_orders",
        port = "5432")

cur=conn.cursor() 

def create_table():
   
   cur.execute(
        """CREATE TABLE IF NOT EXISTS user_address_master (first_name varchar(256),
                                                                    last_name varchar(256),
                                                                    email varchar(256),
                                                                    address varchar(256),
                                                                    created_at timestamp)"""
    )
   conn.commit() 
   conn.close() 

create_table()
header_list = ["first name", "last name", "email", "address", "created at"]
df=pd.read_csv('dataset-medium.csv', names=header_list)

import pandas as pd
 
# read DataFrame
data = pd.read_csv('dataset-medium.csv', names=header_list)
 
# no of csv files with row size
k = 10
size = 30000
 
for i in range(k):
    df = data[size*i:size*(i+1)]
    df.to_csv(f'data-part-{i+1}.csv', index=False)

def send_csv_to_psql(connection,csv,table_):
    sql = "COPY %s FROM STDIN WITH CSV HEADER DELIMITER AS ','"
    file = open(csv, "r")
    table = table_
    with connection.cursor() as cur:
        cur.execute("truncate " + table + ";")  #avoiding uploading duplicate data!
        cur.copy_expert(sql=sql % table, file=file)
        conn.commit()

    return conn.commit()

send_csv_to_psql(conn,'data-part-1.csv','user_address_master')
send_csv_to_psql(conn,'data-part-2.csv','user_address_master')
send_csv_to_psql(conn,'data-part-3.csv','user_address_master')
send_csv_to_psql(conn,'data-part-4.csv','user_address_master')
send_csv_to_psql(conn,'data-part-5.csv','user_address_master')
send_csv_to_psql(conn,'data-part-6.csv','user_address_master')
send_csv_to_psql(conn,'data-part-7.csv','user_address_master')
send_csv_to_psql(conn,'data-part-8.csv','user_address_master')
send_csv_to_psql(conn,'data-part-9.csv','user_address_master')
send_csv_to_psql(conn,'data-part-10.csv','user_address_master')
