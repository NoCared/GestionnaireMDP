from database.Manager import Manager


from flask import Flask, request, jsonify

app = Flask(__name__)

manager = Manager()


# Endpoint pour l'authentification des utilisateurs
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if manager.connect(data.get('username'),data.get('password')):
        return jsonify({'message': 'Authentification réussie'}), 200
    else:
        return jsonify({'message': 'Identifiants incorrects'}), 401

@app.route("/password/create", methods=['POST'])
def create_password():
    data = request.get_json()
    manager.create_password(data.get('site'),data.get('password'))
    return jsonify({'message': 'Authentification réussie'}), 200
    

@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/testBdd")
def testBdd():
    return "Hello, World!"


