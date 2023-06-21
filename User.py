class User():

    def __init__(self, id, userType, username, password):
        self.id = str(id)
        self.userType = str(userType)
        self.username = str(username)
        self.password = str(password)

        idStore = str(self.id).ljust(5)
        userTypeStore = str(self.userType).ljust(1)
        usernameStore = self.username.ljust(10)
        passwordStore = self.password.ljust(10)
        storeFile = open("users.txt", "a")
        storeInfo = idStore + userTypeStore + usernameStore + passwordStore + "\n"
        storeFile.write(storeInfo)
        storeFile.close()

    def setID(self, id):
        self.id = id

    def getID(self):
        return self.id

    def setUserType(self, userType):
        self.userType = userType

    def getUserType(self):
        return self.userType

    def setUsername(self, username):
        self.username = username

    def getUsername(self):
        return self.username

    def setPassword(self, password):
        self.password = password

    def getPassword(self):
        return self.password

    #Needs testing
    def updateStoredDetails(self, id, userType, username, password):
        self.setID(id)
        self.setUserType(userType)
        self.setUsername(username)
        self.setPassword(password)
        with open("users.txt", "a") as file:
            data = file.readlines()
            for line in data:
                if id == line[0]:
                    userTypeStore = str(self.userType).ljust(1)
                    usernameStore = self.username.ljust(10)
                    passwordStore = self.password.ljust(10)
                    storeInfo = userTypeStore + usernameStore + passwordStore + "\n"
                    data[data.index(line)] = storeInfo




