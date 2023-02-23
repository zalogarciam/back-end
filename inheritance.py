class Person:
    def __init__(self,name, last_name):
        self.name = name
        self.last_name = last_name

    def say_hi(self):
        return "GM"
    
class Benefit:
    def __init__(self, detail):
        self.detail = detail

    def show(self):
        return {
            'detail': self.detail
        }
    
class Student(Person):
    def __init__(self, name, last_name, level):
        self.level = level
        super().__init__(name, last_name)

    def say_hi(self):
        hi = super().say_hi()
        print(hi + ", " + "I am a student")
    
    def walking_around(self):
        print("Walk ...")

    
class Teacher(Person, Benefit):
    def __init__(self, name, last_name, social_number, detail):
        self.social_number = social_number
        Person.__init__(self, name, last_name)
        Benefit.__init__(self, detail)

    def evaluate(self):
        print("Evaluate ...")


gonzalo = Student('Gonzalo', 'Garcia', 'Last Year')
eduardo = Teacher('Eduardo', 'Garcia', 123, 'Detail')

gonzalo.say_hi()
print(eduardo.say_hi())

print(eduardo.show())
print(eduardo.name)


