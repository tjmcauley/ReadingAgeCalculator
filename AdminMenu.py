from MainMenu import *


def createAdminMenu():
    print("""
                 ~########################################################~
                 ~#                                                      #~
                 ~#                                                      #~
                 ~# ______________       __________            ___       #~
                 ~# |              |     |          \         /   \      #~
                 ~# |              |     |   _____   \       /  _  \     #~
                 ~# `````|    |`````     |  |     \   \     /  / \  \    #~
                 ~#      |    |          |  |      \  |    /  /   \  \   #~
                 ~#      |    |          |  |       | |   /  /     \  \  #~
                 ~#      |    |          |  |       | |   |  |_____|  |  #~
                 ~#      |    |          |  |      /  |   |   _____   |  #~
                 ~#  ____|    |____      |  |_____/   /   |  |     |  |  #~
                 ~# |              |     |           /    |  |     |  |  #~
                 ~# |______________|     |__________/     |__|     |__|  #~
                 ~#                                                      #~
                 ~#                      DEWISLEN ADMIN                  #~
                 ~#                                                      #~
                 ~#                     (1) Allgofnodi                   #~
                 ~#               (2) Creu defnyddiwr arferol            #~
                 ~#           (3) Mewngofnodi fel defnyddiwr arferol     #~
                 ~########################################################~

                 Beth hoffech chi gwneud?:
                 """)

    while True:
        try:
            userIn = int(input())
            if userIn == 1:
                createMainMenu()
                break
            elif userIn == 2:
                createUser()
                break
            elif userIn == 3:
                login()
                break
            else:
                print("Yn anffodus nad yw'r opsiwn yna ar gael")
        except ValueError:
            print("Yn anffodus nad yw'r opsiwn yna ar gael")


def createUser(self):
    while True:
        try:
            userTypeSelect = int(input("Pa fath o ddefnyddiwr hoffech chi creu; (-1)gadael (1)admin (2)arferol: "))
            if userTypeSelect == -1:
                createAdminMenu()
            elif userTypeSelect < -1 or userTypeSelect == 0 or userTypeSelect > 2:
                print("Yn anffodus nad yw'r opsiwn yna ar gael")
            else:
                break
        except ValueError:
            print("Yn anffodus nad yw'r opsiwn yna ar gael")

    while True:
        username = str(input("Mewnbynnwch eich enw defnyddiwr: "))
        if len(username) > 10:
            print("Mae rhaid i'r enw defnyddiwr bod yn llai nag 11 nod")
        else:
            break

    while True:
        pass1 = str(input("Mewnbynnwch eich cyfrinair: "))
        if len(pass1) > 10:
            print("Mae rhaid i'r cyfrinair bod yn llai nag 11 nod")
        else:
            pass2 = str(input("Mewnbynnwch eich cyfrinair eto: "))
            if pass1 != pass2:
                print("Mae rhaid i'r cyfrineiriau cyfateb i'w gilydd")
            else:
                break

    userTypeStore = str(userTypeSelect).ljust(1)
    usernameStore = username.ljust(10)
    passwordStore = pass2.ljust(10)
    storeFile = open("users.txt", "a")
    storeInfo = userTypeStore + usernameStore + passwordStore + "\n"
    storeFile.write(storeInfo)
    storeFile.close()
    print("Wedi storio;\nMath Defnyddiwr: " + userTypeStore
          + "\nEnw Defnyddiwr: " + usernameStore
          + "\nCyfrinair: **********")
    createAdminMenu()


def login(self):
    usernameInput = str(input("Mewnbynnwch eich enw defnyddiwr: "))
    passwordInput = str(input("Mewnbynnwch eich cyfrinair: "))

    try:
        readUser = open("users.txt", "r")
    except FileNotFoundError:
        print("Nad oedd y ffeil users.txt yn gallu cael ei ddarganfod")

    while True:
        userLocation = readUser.readline()
        validateUserType = userLocation[0:1].strip()
        validateUsername = userLocation[1:11].strip()
        validatePassword = userLocation[11:21].strip()
        if userLocation == "":
            readUser.close()
            print("Nad oedd y defnyddiwr yna'n gallu cael ei ddarganfod")
            createAdminMenu()
        elif validateUserType == str(
                1) and validateUsername == usernameInput and validatePassword == passwordInput:
            createAdminMenu()
            break
        elif validateUserType == str(
                2) and validateUsername == usernameInput and validatePassword == passwordInput:
            createAdminMenu()
            break
