# import relevant packages

import requests
import json
import psycopg2

# use requests to make get call

response = requests.get("https://api.hubapi.com/engagements/v1/engagements/paged?hapikey=demo")

# store JSON object in variable

j = response.json()

# connect to postgresql and activate cursor for queries

conn = psycopg2.connect(dbname="postgres", user="postgres", password="password")
cur = conn.cursor()

# create table to store engagement details

cur.execute("CREATE TABLE engagements (id bigint, type varchar, timestamp bigint);")

# use while loop to read all json objects and insert into table

i = 0
while i < (len(j['results'])):
	cur.execute("INSERT INTO engagements (id, type, timestamp) VALUES (%s, %s, %s)", (j['results'][i]['engagement']['id'], j['results'][i]['engagement']['type'], j['results'][i]['engagement']['timestamp']))
	i += 1
	
# check for the number of days between the first and last engagement
	
cur.execute("select ((max(timestamp)) - (min(timestamp)))/86400000 from engagements;")

# retrieve results

cur.fetchall()