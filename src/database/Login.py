from database.Database import Database


def login(user, password):
    try:
        db = Database("GestionnaireMDP", user=user, password=password)
        print("Authentification réussie !")
        return db
    except Exception as e:
        print(f"Erreur d'authentification : {e}")
        return None

def connect(user,password):
    db = login(user, password)

    if db is not None:
        # L'authentification a réussi, vous pouvez procéder à d'autres opérations ici
        return True
    else:
        # Gérer l'échec d'authentification
        return False