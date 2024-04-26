import psycopg2


class Database:
    def __init__(self,database):
        self.connect(database)
        self.cursor = self.db.cursor()
        
    def execute(self,sql):
        self.cursor.execute(sql)
        
    def commit(self):
        self.db.commit()
    
    def close(self):
        self.cursor.close()
        self.db.close()

    def connect(self,database):
        self.db = psycopg2.connect(
        host="db",
        user="paul",
        password="paul",
        database=database
        )

    def initdatas(self):
        create_table_query = ''' CREATE TABLE IF NOT EXISTS test_table (id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL, age INT )'''
        self.execute(create_table_query)
        self.commit()