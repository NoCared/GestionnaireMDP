import tkinter as tk
from database.Database import Database

class AuthGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Authentification")

        self.label_user = tk.Label(master, text="User:")
        self.label_user.grid(row=1, column=0)
        self.entry_user = tk.Entry(master)
        self.entry_user.grid(row=1, column=1)

        self.label_password = tk.Label(master, text="Password:")
        self.label_password.grid(row=2, column=0)
        self.entry_password = tk.Entry(master, show="*")
        self.entry_password.grid(row=2, column=1)

        self.button_login = tk.Button(master, text="Login", command=self.login)
        self.button_login.grid(row=3, column=0, columnspan=2)

        self.db = None

    def login(self):
        user = self.entry_user.get()
        password = self.entry_password.get()

        try:
            self.db = Database("GestionnaireMDP", user=user, password=password)
            print("Authentification réussie !")
            self.master.destroy()  # Ferme la fenêtre après l'authentification réussie
        except Exception as e:
            print(f"Erreur d'authentification : {e}")

def main():
    root = tk.Tk()
    app = AuthGUI(root)
    root.mainloop()

    if app.db is not None:
        # L'authentification a réussi, vous pouvez procéder à d'autres opérations ici
        pass
    else:
        # L'utilisateur a fermé la fenêtre sans s'authentifier, vous pouvez quitter le programme ou gérer l'erreur
        pass

if __name__ == "__main__":
    main()