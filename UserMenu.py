import MainMenu as MM
import math


class UserMenu():

    def __init__(self):
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
                 ~#         (5) Chwilio am destun trwy sgor darllen      #~
                 ~########################################################~

                 Beth hoffech chi gwneud?:
                 """)

        while True:
            try:
                userIn = int(input())
                if userIn == 1:
                    MM.MainMenu()
                    break
                elif userIn == 2:
                    self.inputText()
                    break
                elif userIn == 3:
                    self.keywordSearch()
                    break
                elif userIn == 4:
                    self.titleSearch()
                    break
                elif userIn == 5:
                    self.ageSearch()
                    break
                else:
                    print("Yn anffodus nad yw'r opsiwn yna ar gael")
            except ValueError:
                print("Yn anffodus nad yw'r opsiwn yna ar gael")

    def inputText(self):
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
                UserMenu()
            elif sentenceCount < 5:
                print("Mae'r testun yn rhy byr, mewnbynnwch testun hirrach")
                UserMenu()
            else:
                IDAValue = math.ceil(4.71 * (characterCount / wordCount) + 0.5 * (wordCount / sentenceCount) - 21.43)

                if IDAValue == 1:
                    Age = "5-6"
                    Year = "1"
                elif IDAValue == 2:
                    Age = "6-7"
                    Year = "2"
                elif IDAValue == 3:
                    Age = "7-8"
                    Year = "3"
                elif IDAValue == 4:
                    Age = "8-9"
                    Year = "4"
                elif IDAValue == 5:
                    Age = "9-10"
                    Year = "5"
                elif IDAValue == 6:
                    Age = "10-11"
                    Year = "6"
                elif IDAValue == 7:
                    Age = "11-12"
                    Year = "7"
                elif IDAValue == 8:
                    Age = "12-13"
                    Year = "8"
                elif IDAValue == 9:
                    Age = "13-14"
                    Year = "9"
                elif IDAValue == 10:
                    Age = "14-15"
                    Year = "10"
                elif IDAValue == 11:
                    Age = "15-16"
                    Year = "11"
                elif IDAValue == 12:
                    Age = "16-17"
                    Year = "12"
                else:
                    Age = "17+"
                    Year = "Arall"
                print(
                    "Yr oedran sy'n cael ei argymell ar gyfer y testun yma yw: " + Age + " sef mewn blwyddyn: " + Year)
        except ZeroDivisionError:
            print("Mae'r testun yn rhy byr, mewnbynnwch testun hirrach")
            UserMenu()

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

                readingAgeStore = str(IDAValue).ljust(3)
                titleStore = titleIn.ljust(35)
                keyword1Store = keyword1In.ljust(15)
                keyword2Store = keyword2In.ljust(15)
                keyword3Store = keyword3In.ljust(15)
                keyword4Store = keyword4In.ljust(15)
                keyword5Store = keyword5In.ljust(15)
                textStore = textIn.ljust(2000)

                storeFile = open("storedText.txt", "a")
                storeInfo = readingAgeStore + titleStore + keyword1Store + keyword2Store + keyword3Store \
                            + keyword4Store + keyword5Store + textStore + "\n"

                storeFile.write(storeInfo)
                storeFile.close()
                print("Wedi storio: " + titleStore)
                UserMenu()
                break

            elif storeIn == "n":
                UserMenu()
                break
            else:
                print("Yn anffodus nad yw'r opsiwn yna ar gael")

    def keywordSearch(self):
        keywordIn = str(input("Mewnbynnwch allweddair: "))

        try:
            readTextFile = open("storedText.txt", "r")
        except FileNotFoundError:
            print("Nad oedd y ffeil storedText.txt yn gallu cael ei ddarganfod")

        while True:
            location = readTextFile.readline()

            readingAge = location[0:3].strip()
            title = location[3:38].strip()
            keyword1 = location[38:53].strip()
            keyword2 = location[53:68].strip()
            keyword3 = location[68:83].strip()
            keyword4 = location[83:98].strip()
            keyword5 = location[98:113].strip()
            text = location[113:2113]

            if (location == ""):
                readTextFile.close()
                UserMenu()
                break
            elif (keywordIn == keyword1 or keywordIn == keyword2 or keywordIn == keyword3
                    or keywordIn == keyword4 or keywordIn == keyword5):
                print("Dyma'r testunau mwyaf perthnasol:\n")
                print("Oedran darllen y testun yw: " + readingAge)
                print(title)
                print(text)

    def titleSearch(self):
        titleIn = str(input("Mewnbynnwch teitl y testun: "))

        try:
            readTextFile = open("storedText.txt", "r")
        except FileNotFoundError:
            print("Nad oedd y ffeil storedText.txt yn gallu cael ei ddarganfod")

        while True:
            location = readTextFile.readline()

            readingAge = location[0:3].strip()
            title = location[3:38].strip()
            keyword1 = location[38:53].strip()
            keyword2 = location[53:68].strip()
            keyword3 = location[68:83].strip()
            keyword4 = location[83:98].strip()
            keyword5 = location[98:113].strip()
            text = location[113:2113]

            print(title)

            if (location == ""):
                readTextFile.close()
                UserMenu()
                break
            elif (titleIn == title):
                print("Dyma'r testunau mwyaf perthnasol:\n")
                print("Oedran darllen y testun yw: " + readingAge)
                print(title)
                print(text)

    def ageSearch(self):
        ageIn = str(input("Mewnbynnwch sgor darllen y testun: "))

        try:
            readTextFile = open("storedText.txt", "r")
        except FileNotFoundError:
            print("Nad oedd y ffeil storedText.txt yn gallu cael ei ddarganfod")

        while True:
            location = readTextFile.readline()

            readingAge = location[0:3].strip()
            title = location[3:38].strip()
            keyword1 = location[38:53].strip()
            keyword2 = location[53:68].strip()
            keyword3 = location[68:83].strip()
            keyword4 = location[83:98].strip()
            keyword5 = location[98:113].strip()
            text = location[113:2113]

            if (location == ""):
                readTextFile.close()
                print("Nad oedd darn darllen yn gallu cael ei ddarganfod")
                UserMenu()
                break
            elif (ageIn == readingAge):
                print("Dyma'r testunau mwyaf perthnasol:\n")
                print("Oedran darllen y testun yw: " + readingAge)
                print(title)
                print(text)