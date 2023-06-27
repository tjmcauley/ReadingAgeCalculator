import MainMenu
import math


def createUserMenu():
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
                 ~#                      DEWISLEN DEFNYDDIWR             #~
                 ~#                                                      #~
                 ~#                     (1) Allgofnodi                   #~
                 ~#              (2) Mewnbynnu Testun a'i storio         #~
                 ~#         (3) Chwilio am destun trwy allweddeiriau     #~
                 ~#             (4) Chwilio am destun trwy'r teitl       #~
                 ~#         (5) Chwilio am destun trwy oedran darllen      #~
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
                storeText()
                break
            elif userIn == 3:
                keywordSearch()
                break
            elif userIn == 4:
                titleSearch()
                break
            elif userIn == 5:
                ageSearch()
                break
            else:
                print("Yn anffodus nad yw'r opsiwn yna ar gael")
        except ValueError:
            print("Yn anffodus nad yw'r opsiwn yna ar gael")

def storeText():
    textIn = str(input("Mewnbynnwch y darn testun er mwyn storio a cyfrifo'r oedran darllen (max 2000 nod):"))

    spaceCount = textIn.count(" ")
    characterCount = len(textIn)
    fullStopCount = textIn.count(".")
    questionMarkCount = textIn.count("?")
    exclamationMarkCount = textIn.count("!")
    wordCount = spaceCount + 1
    sentenceCount = (fullStopCount + questionMarkCount + exclamationMarkCount)

    try:
        if characterCount > 2000:
            print("Mae'r testun yn rhy hir, mewnbynnwch testun byrrach")
            createUserMenu()
        elif sentenceCount < 5:
            print("Mae'r testun yn rhy byr, mewnbynnwch testun hirrach")
            createUserMenu()
        else:
            IDAValue = math.ceil(4.71 * (characterCount / wordCount) + 0.5 * (wordCount / sentenceCount) - 21.43)

            if IDAValue == 1:
                age = "5-6"
                year = "1"
            elif IDAValue == 2:
                age = "6-7"
                year = "2"
            elif IDAValue == 3:
                age = "7-8"
                year = "3"
            elif IDAValue == 4:
                age = "8-9"
                year = "4"
            elif IDAValue == 5:
                age = "9-10"
                year = "5"
            elif IDAValue == 6:
                age = "10-11"
                year = "6"
            elif IDAValue == 7:
                age = "11-12"
                year = "7"
            elif IDAValue == 8:
                age = "12-13"
                year = "8"
            elif IDAValue == 9:
                age = "13-14"
                year = "9"
            elif IDAValue == 10:
                age = "14-15"
                year = "10"
            elif IDAValue == 11:
                age = "15-16"
                year = "11"
            elif IDAValue == 12:
                age = "16-17"
                year = "12"
            else:
                age = "17+"
                year = "Arall"
            print(
                "Yr oedran sy'n cael ei argymell ar gyfer y testun yma yw: " + age + " sef mewn blwyddyn: " + year)
    except ZeroDivisionError:
        print("Mae'r testun yn rhy byr, mewnbynnwch testun hirrach")
        createUserMenu()

    while True:
        storeIn = str(input("Hoffech chi storio'r testun yma? (Y/N):")).lower()
        if storeIn == "y":
            while True:
                titleIn = str(input("Mewnbynnwch teitl y darn darllen (max 35 nod): "))
                if len(titleIn) > 35:
                    print("Mae'r teitl yn rhy hir")
                else:
                    break

            while True:
                keyword1In = str(input("Mewnbynnwch allweddair 1 (max 15 nod): "))
                if len(keyword1In) > 15:
                    print("Mae'r allweddair yn rhy hir")
                else:
                    break

            while True:
                keyword2In = str(input("Mewnbynnwch allweddair 2 (max 15 nod): "))
                if len(keyword2In) > 15:
                    print("Mae'r allweddair yn rhy hir")
                else:
                    break

            while True:
                keyword3In = str(input("Mewnbynnwch allweddair 3 (max 15 nod): "))
                if len(keyword3In) > 15:
                    print("Mae'r allweddair yn rhy hir")
                else:
                    break

            while True:
                keyword4In = str(input("Mewnbynnwch allweddair 4 (max 15 nod): "))
                if len(keyword4In) > 15:
                    print("Mae'r allweddair yn rhy hir")
                else:
                    break

            while True:
                keyword5In = str(input("Mewnbynnwch allweddair 5 (max 15 nod): "))
                if len(keyword5In) > 15:
                    print("Mae'r allweddair yn rhy hir")
                else:
                    break

            readingAgeStore = age.ljust(5)
            titleStore = titleIn.ljust(35)
            keyword1Store = keyword1In.ljust(15)
            keyword2Store = keyword2In.ljust(15)
            keyword3Store = keyword3In.ljust(15)
            keyword4Store = keyword4In.ljust(15)
            keyword5Store = keyword5In.ljust(15)
            textStore = textIn.ljust(2000)

            storeFile = open("Texts.txt", "a")
            storeInfo = readingAgeStore + titleStore + keyword1Store + keyword2Store + keyword3Store \
                        + keyword4Store + keyword5Store + textStore + "\n"

            storeFile.write(storeInfo)
            storeFile.close()
            print("Wedi storio: " + titleStore)
            createUserMenu()
            break

        elif storeIn == "n":
            createUserMenu()
            break
        else:
            print("Yn anffodus nad yw'r opsiwn yna ar gael")


def keywordSearch():
    keywordIn = str(input("Mewnbynnwch allweddair: "))

    try:
        readTextFile = open("Texts.txt", "r")
    except FileNotFoundError:
        print("Nad oedd y ffeil Texts.txt yn gallu cael ei ddarganfod")

    while True:
        location = readTextFile.readline()

        readingAge = location[0:5].strip()
        title = location[5:40].strip()
        keyword1 = location[40:55].strip()
        keyword2 = location[55:70].strip()
        keyword3 = location[70:85].strip()
        keyword4 = location[85:100].strip()
        keyword5 = location[100:115].strip()
        text = location[115:2115]

        if (location == ""):
            readTextFile.close()
            createUserMenu()
            break
        elif (keywordIn == keyword1 or keywordIn == keyword2 or keywordIn == keyword3
              or keywordIn == keyword4 or keywordIn == keyword5):
            print("Dyma'r testunau mwyaf perthnasol:\n")
            print("Oedran darllen y testun yw: " + readingAge)
            print(title)
            print(text)


def titleSearch():
    titleIn = str(input("Mewnbynnwch teitl y testun: "))

    try:
        readTextFile = open("Texts.txt", "r")
    except FileNotFoundError:
        print("Nad oedd y ffeil Texts.txt yn gallu cael ei ddarganfod")

    while True:
        location = readTextFile.readline()

        readingAge = location[0:5].strip()
        title = location[5:40].strip()
        keyword1 = location[40:55].strip()
        keyword2 = location[55:70].strip()
        keyword3 = location[70:85].strip()
        keyword4 = location[85:100].strip()
        keyword5 = location[100:115].strip()
        text = location[115:2115]

        print(title)

        if (location == ""):
            readTextFile.close()
            createUserMenu()()
            break
        elif (titleIn == title):
            print("Dyma'r testunau mwyaf perthnasol:\n")
            print("Oedran darllen y testun yw: " + readingAge)
            print(title)
            print(text)


def ageSearch():
    ageIn = str(input("Mewnbynnwch oedran darllen y testun: "))

    try:
        readTextFile = open("Texts.txt", "r")
    except FileNotFoundError:
        print("Nad oedd y ffeil Texts.txt yn gallu cael ei ddarganfod")

    while True:
        location = readTextFile.readline()

        readingAge = location[0:5].strip()
        title = location[5:40].strip()
        keyword1 = location[40:55].strip()
        keyword2 = location[55:70].strip()
        keyword3 = location[70:85].strip()
        keyword4 = location[85:100].strip()
        keyword5 = location[100:115].strip()
        text = location[115:2115]

        if (location == ""):
            readTextFile.close()
            print("Nad oedd darn darllen yn gallu cael ei ddarganfod")
            createUserMenu()()
            break
        elif (ageIn == readingAge):
            print("Dyma'r testunau mwyaf perthnasol:\n")
            print("Oedran darllen y testun yw: " + readingAge)
            print(title)
            print(text)
