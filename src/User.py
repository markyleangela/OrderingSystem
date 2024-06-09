class User:

    __username = None
    __password = None

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password
    
    def setUsername(self, username):
        self.username = username

    def setPassword(self, password):
        self.password = password

    def logOut():
        pass


    def addToOrder():
        pass

    def removeOrder():
        pass

    def submitOrder():
        pass

    def clearOrder():
        pass
    
    def previewReceipt():
        pass

    def viewProduct():
        pass