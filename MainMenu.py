from AdminMenu import *
from UserMenu import *


class MainMenu():

    def __init__(self):
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
                    self.createUser()
                    break
                elif userIn == 3:
                    self.login()
                    break
                elif userIn == 4:
                    self.aboutUs()
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
                    MainMenu()
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
        MainMenu()

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
                MainMenu()
            elif validateUserType == str(
                    1) and validateUsername == usernameInput and validatePassword == passwordInput:
                AdminMenu()
                break
            elif validateUserType == str(
                    2) and validateUsername == usernameInput and validatePassword == passwordInput:
                UserMenu()
                break

    def aboutUs(self):
        print("Yr IDA yw rhaglen sydd wedi cael ei ddylunio er mwyn cyfrifo oedran darllen testun sy'n\n "
              "cael ei mewnbynnu (llai na 2000 nod). Ar ôl mewnbynnu a cyfrifo'r oedran darllen bydd hi'n\n "
              "cael ei storio i ddarn testun. Mae hyn yn ddefnyddiol ar gyfer athrawon sydd eisiau dod o\n "
              "hyd i ddarn darllen addas ar gyfer ei ddosbarth gan sicrhau nad yw'n rhy heriol. Bydd rhaid\n "
              "i chi creu cyfrif cyn iddych chi defnyddio'r rhaglen.")
        MainMenu()
