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
        """CREATE TABLE IF NOT EXISTS user_address_2018_snapshots (first_name varchar(256),
                                                                    last_name varchar(256),
                                                                    email varchar(256),
                                                                    address varchar(256),
                                                                    created_at timestamp)"""
    )
   conn.commit() 
   conn.close() 

create_table()

header_list = ["first name", "last name", "email", "address", "created at"]
df=pd.read_csv('dataset-small.csv', names=header_list)

df['created at'] = pd.to_datetime(df['created at'], format='%Y-%m-%dT%H:%M:%S')

df=df[(df['created at'] >= '2018-02-01 00:00:00.000000+00:00') & (df['created at'] <= '2018-12-31 00:00:00.000000+00:00')]

df=df.sort_values(by=["created at"], ascending=True)

df.to_csv('filterdata.csv', header=df.columns, index=False, encoding='utf-8')
my_file=open('filterdata.csv')

def send_csv_to_psql(connection,csv,table_):
    sql = "COPY %s FROM STDIN WITH CSV HEADER DELIMITER AS ','"
    file = open(csv, "r")
    table = table_
    with connection.cursor() as cur:
        cur.execute("truncate " + table + ";")  #avoiding uploading duplicate data!
        cur.copy_expert(sql=sql % table, file=file)
        conn.commit()

    return conn.commit()

send_csv_to_psql(conn,'filterdata.csv','user_address_2018_snapshots')

a="user_address_2018_snapshots"
sql_="SELECT COUNT (*) FROM user_address_2018_snapshots"
b=cur.execute(sql_)
b=cur.fetchone()
sql_2="SELECT MAX(created_at) FROM user_address_2018_snapshots"
c=cur.execute(sql_2)
c=cur.fetchone()
print("job is finish. table '{}' has {} rows and last created_at is {}".format(a, b, c))
