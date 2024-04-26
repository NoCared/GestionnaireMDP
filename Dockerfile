# Utilisez une image Python officielle en tant que base
FROM python:3.9

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez le fichier requirements.txt depuis le dossier src/ dans le conteneur
COPY ./src/requirements.txt .

# Installez les dépendances définies dans requirements.txt
RUN pip install -r requirements.txt

# Copiez tout le contenu du dossier src/ dans le conteneur
COPY ./src/ .

# Commande par défaut à exécuter lorsque le conteneur est démarré
CMD ["python", "app.py"]
