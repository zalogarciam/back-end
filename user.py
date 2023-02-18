class User:
    def __init__(self, name, age, id, height, civil_status):
        self.name = name
        self.age = age
        self.id = id
        self.height = height
        self.civil_status = civil_status
    
    def to_dict(self):
        dict = {
            "name": self.name,
            "age": self.age,
            "id": self.id,
            "height": self.height,
            "civil_status": self.civil_status
        }
        return dict

user = User("zalo", 99, 123456, 180, "S")
print(user.to_dict())