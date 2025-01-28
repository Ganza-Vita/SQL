import psycopg2

# connect to database
with psycopg2.connect(
        host='localhost',
        database='northwind',
        user='postgres',
        password='12345'
) as conn:
    with conn.cursor() as cur:
        # execution query
        cur.execute("INSERT INTO user_account VALUES (%s, %s)", (6, 'John'))
        cur.execute("SELECT * FROM user_account")
        rows = cur.fetchall()
        for row in rows:
            print(row)



conn.close()
