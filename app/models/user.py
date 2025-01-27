class User:  # Klasa użytkownika
    def __init__(self, user_id, name, surname, email):
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