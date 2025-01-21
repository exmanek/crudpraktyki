from flask import Flask, request, jsonify, make_response

class User: #klasa uzytkownika
    def __init__(self,user_id, name,surname,email):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.email = email

    def to_json(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
        }

app = Flask(__name__)
app.json.sort_keys = False #nie sortuje w postmanie

data_store = [] #pamiec ram

def create_app():

    #CREATE
    @app.route('/api/',methods=['POST'])
    def create_user():
        #pobieramy dane
        user_id = len(data_store) + 1 #problemy z id (baza danych rozwiaze problem)
        name = request.json.get("name")
        surname = request.json.get("surname")
        email = request.json.get("email")

        user = User(user_id,name,surname,email) #tworzymy uzytkownika

        data_store.append(user) #dodajemy uzytkownika
        response_data = {
            "success": True,
            "data": user.to_json()
        }
        return make_response(jsonify(response_data), 201)

    #READ
    @app.route('/api/users',methods=['GET'])
    def get_users():
        response_data = {
            "success": True,
            "data": [user.to_json() for user in data_store]
        }
        return make_response(jsonify(response_data), 200)

    #UPDATE
    @app.route('/api/users/<int:user_id>',methods=["PUT"])
    def update_user(user_id):
        if user_id < 1 or user_id > len(data_store):
            return make_response("User not found",404)
        updated_data = request.json
        user = data_store[user_id - 1]

        user.name = request.json.get("name", user.name)
        user.surname = request.json.get("surname", user.surname)
        user.email = request.json.get("email", user.email)

        response_data = {
            "success": True,
            "data": user.to_json()
        }
        return make_response(jsonify(response_data), 200)

    #DELETE
    @app.route('/api/users/<int:user_id>',methods=["DELETE"])
    def delete_user(user_id):
        if user_id < 1 or user_id > len(data_store):
            return make_response("User not found",404)
        data_store.pop(user_id - 1)

        response_data = {
            "success": True,
            "data": []  #pamietac o response data
        } #wywalic to
        return make_response(jsonify(response_data), 200)
    return app


# obsluga bledow
# dodanie notatek

