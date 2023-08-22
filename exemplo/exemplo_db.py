import psycopg2

conn = psycopg2.connect(host='db', database='postgres',
user='postgres', password='postgres')

cur = conn.cursor()

sql = 'create table cidade (id serial primary key, nome varchar(100), uf varchar(2))'
cur.execute(sql)
sql = "insert into cidade values (default,'São Paulo','SP')"
cur.execute(sql)
conn.commit()
cur.execute('select * from cidade')
recset = cur.fetchall()

for rec in recset:
    print(rec)

cur.close()
conn.close()