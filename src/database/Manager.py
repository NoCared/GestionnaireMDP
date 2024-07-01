from database.Database import Database

class Manager:
    def login(self,user, password):
        try:
            self.db = Database("GestionnaireMDP", user=user, password=password)
            print("Authentification réussie !")
            return self.db
        except Exception as e:
            print(f"Erreur d'authentification : {e}")
            return None

    def connect(self, user,password):
        self.db = self.login(user, password)
        if self.db is not None:
            self.db.initdatas()
            return True
        else:
            # Gérer l'échec d'authentification
            return False
        
    def create_password(self,site,password):
        if self.db is not None:
            create_password_query = '''INSERT INTO mdp_table (site, password) VALUES (%s, %s)'''
            self.db.execute(create_password_query, (site, password))
            self.db.commit()