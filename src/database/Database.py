import psycopg2


class Database:
    def __init__(self,database,user,password):
        self.connect(database,user,password)
        self.cursor = self.db.cursor()
        
    def execute(self,sql,params= None):
        if params:
            print("bla")
            self.cursor.execute(sql, params)
        else:
            self.cursor.execute(sql)
        
    def commit(self):
        self.db.commit()
    
    def close(self):
        self.cursor.close()
        self.db.close()
    def test():
        print('test')

    def connect(self,database,user,password):
        self.db = psycopg2.connect(
        host="db",
        user=user,
        password=password,
        database=database
        )

    def initdatas(self):
        create_table_query = ''' CREATE TABLE IF NOT EXISTS mdp_table (id SERIAL PRIMARY KEY, site VARCHAR(255) NOT NULL, password VARCHAR(255) )'''
        self.execute(create_table_query)
        self.commit()
