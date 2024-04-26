import psycopg2


mydb = psycopg2.connect(
  host="db",
  user="paul",
  password="paul",
  database="GestionnaireMDP"
)


cur = mydb.cursor()

# Requête SQL pour créer une table
create_table_query = '''
    CREATE TABLE IF NOT EXISTS test_table (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        age INT
    )
'''

# Exécution de la requête SQL
cur.execute(create_table_query)

# Validation des changements dans la base de données
mydb.commit()

# Fermeture du curseur et de la connexion
cur.close()
mydb.close()