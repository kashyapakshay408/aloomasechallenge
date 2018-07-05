# check number of engagements by type in dataset

cur.execute("select type, count(id) from engagements group by type")

# retrieve results

cur.fetchall()