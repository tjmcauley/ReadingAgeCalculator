import AdminMenu
import UserMenu
import User
from random import randint

def createMainMenu():
    print("""
             ~########################################################~
             ~#                                                      #~
             ~#                                                      #~
             ~# ______________       __________            ___        ~
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
             ~#                                                      #~s
             ~#                      PRIF DEWISLEN                   #~
             ~#                                                      #~
             ~#                       (1) Gadael                     #~
             ~#                       (2) Creu defnyddiwr            #~
             ~#                       (3) Mewnbynnu                  #~
             ~#                       (4) Amdanyn ni                 #~
             ~########################################################~

             Beth hoffech chi gwneud?:
             """)

    while True:
        try:
            userIn = int(input())
            if userIn == 1:
                quit()
                break
            elif userIn == 2:
                createUser()
                break
            elif userIn == 3:
                login()
                break
            elif userIn == 4:
                aboutUs()
                break
            else:
                print("Yn anffodus nad yw'r opsiwn yna ar gael")
        except ValueError:
            print("Yn anffodus nad yw'r opsiwn yna ar gael")


def createUser():
    userID = randint(100, 999)
    print(userID)
    while True:
        try:
            userTypeSelect = int(input("Pa fath o ddefnyddiwr hoffech chi creu; (-1)gadael (1)admin (2)arferol: "))
            if userTypeSelect == -1:
                createMainMenu()
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
    newUser = User(userID, userTypeSelect, username, pass2)
    print("Wedi storio;\nMath Defnyddiwr: " + newUser.getUserType()
          + "\nEnw Defnyddiwr: " + newUser.getUsername()
          + "\nCyfrinair: **********")
    createMainMenu()


def login():
    usernameInput = str(input("Mewnbynnwch eich enw defnyddiwr: "))
    passwordInput = str(input("Mewnbynnwch eich cyfrinair: "))

    with open("users.txt", "r") as file:
        data = file.readlines()
        for line in data:
            userTypeLocation = line[5:6].strip()
            usernameLocation = line[6:16].strip()
            passwordLocation = line[16:26].strip()
            if userTypeLocation == "1" and usernameInput == usernameLocation and passwordInput == passwordLocation:
                AdminMenu.createAdminMenu()
            elif userTypeLocation == "2" and usernameInput == usernameLocation and passwordInput == passwordLocation:
                UserMenu.createUserMenu()
        print("Nad oedd y defnyddiwr yna'n gallu cael ei ddarganfod")
        createMainMenu()

def aboutUs():
    print("Yr IDA yw rhaglen sydd wedi cael ei ddylunio er mwyn cyfrifo oedran darllen testun sy'n\n "
          "cael ei mewnbynnu (llai na 2000 nod). Ar ôl mewnbynnu a cyfrifo'r oedran darllen bydd hi'n\n "
          "cael ei storio i ddarn testun. Mae hyn yn ddefnyddiol ar gyfer athrawon sydd eisiau dod o\n "
          "hyd i ddarn darllen addas ar gyfer ei ddosbarth gan sicrhau nad yw'n rhy heriol. Bydd rhaid\n "
          "i chi creu cyfrif cyn iddych chi defnyddio'r rhaglen.")
    createMainMenu()
