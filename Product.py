class Product:
    __name = None
    __price = None
    __quantity = None
    __category = None
    __image = None

    def __init__(self, name, price, quantity, category, image):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        self.image = image


    # getters
    def getName(self):
        return self.name
    
    def getPrice(self):
        return self.price
    
    def getQuantity(self):
        return self.quantity
    
    def getCategory(self):
        return self.category
    
    def getImage(self):
        return self.image
    

    # setters

    def setName(self, name):
        self.name = name
    
    def setPrice(self, price):
        self.price = price

    def setQuantity(self, quantity):
        self.quantity = quantity

    def setQuantity(self, category):
        self.category = category

    def setImage(self, image):
        self.image = image

    def __str__(self):
        return f"{self.name}{", "}{self.price}"

