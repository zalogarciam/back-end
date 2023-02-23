class Chair:
    def __init__(self, height, width, legs):
        self.height = height
        self.width = width
        self.legs = legs

    def print(self):
        return {
            "Height": self.height,
            "Width": self.width,
            "Legs": self.legs
        }

obj = Chair(10, 20, 4)
print(obj.print())