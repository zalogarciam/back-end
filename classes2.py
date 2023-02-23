class Person:
    height = 1.75
    weight = 77
    sign = "Cancer"

    def add(self, *args):
        sum = 0
        for n in args:
            sum += n
        return sum
    def hi(self, name):
        return 'Hola {}'.format(name)
    

person = Person()
print(person.add(10, 5, 41, 526, 489, 63))
print(person.add(5, 8, 65, 985, 491, 520, 700))