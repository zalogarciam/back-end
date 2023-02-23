class Product:
    def __init__(self, name, price, quantity, date):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.date = date
        self.__percentage = 0.3

    def show_percentage(self):
        print(self.__percentage)

pitahaya = Product("pitahaya", 4.5, 100, '2/22/2023')
pitahaya.show_percentage()
