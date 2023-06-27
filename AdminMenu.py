import MainMenu
from User import *

usersArray = []
with open("users.txt", "r") as file:
    data = file.readlines()
    for line in data:
        userID = line[0:5]
        userType = line[5:6]
        username = line[6:16]
        password = line[16:26]
        usersArray.append(User(userID, userType, username, password))


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
                 ~#           (3) Diweddaru manylion defnyddiwr          #~
                 ~#             (4) Dileu manylion defnyddiwr            #~
                 ~########################################################~

                 Beth hoffech chi gwneud?:
                 """)

    while True:
        try:
            userIn = int(input())
            if userIn == 1:
                MainMenu.createMainMenu()
                break
            elif userIn == 2:
                createUser()
                break
            elif userIn == 3:
                updateUserDetails()
                break
            elif userIn == 4:
                deleteUser()
            else:
                print("Yn anffodus nad yw'r opsiwn yna ar gael")
        except ValueError:
            print("Yn anffodus nad yw'r opsiwn yna ar gael")


def createUser():
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

def updateUserDetails():
    userID = str(input("Mewnbynnwch ID y defnyddiwr i newid: "))
    for elem in usersArray:
        if userID in elem.getID():
            while True:
                try:
                    userTypeSelect = int(
                        input("Pa fath o ddefnyddiwr hoffech chi diweddaru i; (-1)gadael (1)admin (2)arferol: "))
                    if userTypeSelect == -1:
                        createAdminMenu()
                    elif userTypeSelect < -1 or userTypeSelect == 0 or userTypeSelect > 2:
                        print("Yn anffodus nad yw'r opsiwn yna ar gael")
                    else:
                        break
                except ValueError:
                    print("Yn anffodus nad yw'r opsiwn yna ar gael")

            while True:
                username = str(input("Mewnbynnwch yr enw defnyddiwr newydd: "))
                if len(username) > 10:
                    print("Mae rhaid i'r enw defnyddiwr bod yn llai nag 11 nod")
                else:
                    break

            while True:
                pass1 = str(input("Mewnbynnwch y cyfrinair newydd: "))
                if len(pass1) > 10:
                    print("Mae rhaid i'r cyfrinair bod yn llai nag 11 nod")
                else:
                    pass2 = str(input("Mewnbynnwch y cyfrinair newydd eto: "))
                    if pass1 != pass2:
                        print("Mae rhaid i'r cyfrineiriau cyfateb i'w gilydd")
                    else:
                        break

            elem.updateStoredDetails(userID, userTypeSelect, username, pass2)
    createAdminMenu()

def deleteUser():
    return
