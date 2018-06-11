class dog:
    legs = 4

    def _init_(self, name, color):
        self.name = name
        self.color = color
        
        fido = dog("fido", "brown")
        print(fido.legs)
        print(dog.legs)
