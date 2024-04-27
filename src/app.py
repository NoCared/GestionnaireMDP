from database.Login import connect


from flask import Flask, request, jsonify

app = Flask(__name__)


# Endpoint pour l'authentification des utilisateurs
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    print (request.json)
    username = data.get('username')
    password = data.get('password')
    if connect(username,password):
        return jsonify({'message': 'Authentification réussie'}), 200
    else:
        return jsonify({'message': 'Identifiants incorrects'}), 401

@app.route('/test', methods=['GET'])
def test():
    return jsonify({'message': 'Test réussi'}), 200

@app.route("/")
def hello():
    return "Hello, World!"


