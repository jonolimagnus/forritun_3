#jón ólafur
#skilaverkefni 1
import math

on = 1
while on ==1:
    print("1 dictionary")
    print("2 listi")
    print("3 skaárvinsla")
    print("4 strengur")
    print("5 hætta")
    val = int(input("veldu milli 1-4"))

    if val ==1:
        safn = {"Hafnafjörður": 220,"Reykjavík":101,"Kópavogur":200,"Garðabær":110,"Akureyri":300,"Moselsbær":221,"Selfoss":250,"miðbær":111}#bý til dictionary
        for k,v in safn.items():#prenta út safnið í nokkrum línum
            print(k,v)
        on = 2
        while on ==2:
            print("1 finnur staðsetningu")
            print("2 bæta við nýju póstnúmeri")
            print("3 eyðir")
            print("4 breytir póstnúmeeri")
            print("5 hætta")
            val = int(input("veldu milli 1-4"))

            if val == 1:
                stadur = input("sláðu inn stað")
                if stadur in safn:
                    print(safn[stadur])
                else:
                    print(stadur,"er ekki til í safninu")

            elif val == 2:
                safn["færeyjar"]=390#bæti við stað og póstnúmeri í safnið
                for k,v in safn.items():
                    print(k,v)
            elif val == 3:
                del safn["miðbær"]#eyði stað frá safninu
                for k,v in safn.items():
                    print(k,v)
            elif val == 4:
                numer = int(input("sláðu inn póstnúmer"))#fær notandann til að breyta póstnúmeri staðs
                safn["færeyjar"]= numer
                for k,v in safn.items():
                    print(k,v)
            elif val == 5:
                on = 0
            else:
                print("þú verður að velja 1-4 og 5 til að hætta")

    elif val ==2:
        tal = int(input("hvað eru margir skráðir í FOR1TÖ05CU"))#læt notanda skrifa út hvað eru margir nemendur í hópnum
        hopur =[]#er listinn með nemendunum í
        for x in range(tal):
            nemendur = input("skrifaðu nöfn þeirra")
            hopur.append(nemendur)
        hopur.sort()
        print(hopur)

        tal2 = int(input("hvað eru margir skráðir í GSÖ1TÖ05AU"))#læt notanda skrifa út hvað eru margir nemendur í hópnum
        hopur2 =[]#bý til seinni listan
        for x in range(tal2):
            nemendur2 = input("skrifaðu nöfn þeirra")#læt notanda skrifa nöfn nemendana
            hopur2.append(nemendur2)
        hopur2.sort()#sett þá í stafrósröð
        print(hopur2)#prenti þá út
        print("a")#prenti hópana út saman og í stafrósröð
        samt = hopur+hopur2
        samt.sort()

        for nemendur in hopur:#prenta út hvern nemenda í sína eiginn línu
            print(nemendur, end=" ")
            print()
        for nemendur2 in hopur2:#geri það sama hér
            print(nemendur2,end=" ")
            print()
        print("b")
        print(samt)#prenti út hopana samman
        print("c hver hópur er stærri")
        if hopur < hopur2:
            print("FOR1TÖ05CU er stærri")
        if hopur > hopur2:
            print("GSÖ1TÖ05AU er stærri")
        if hopur == hopur2:
            print("þeir eru jafnstórir")
        print("d")#tek siðustu tvo nofninn úr fyrsta hópnum og sett það í seinni hópinn
        hopur.remove(-2)
        hopur.remove(-1)
        hopur2.insert(-2,hopur[-2])
        hopur2.insert(-1,hopur[-1])
        print(hopur2)

    elif val ==3:
        def lesa_skra(lykilord):
            with open("lykilord.txt","r",encoding = "utf-8") as f:
                texti=f.read()
                skra=texti.split()
            return skra

        lykilord= {"jónas":"jarðaber","haraldur":"kók","konni":"kaffi","jóna":"jól","palli":"páfagaukur","annar":"ananas","elvar":"epli","eymar":"ekkert","anna":"akkeri","kristin":"kennsla","daniel":"dropsteinn"}
        #bý til dictionary með lykilorðanum

        with open("lykilord.txt","w",encoding="utf-8") as f:#bý til skrána með lykil orðunum
            f.write(str(lykilord))#sytt dictionary í skrá
        print(lesa_skra("lykilord.txt"))
        user= input("sláðu inn notandanafn")
        lykil=input("sláðu inn lykilorð")
        flag=True
        for k,v in lykilord.items():
            if user ==k:
                print(user,k)
                if lykil ==v:
                    print("velkominn")
                    flag=False
                    break
                else:
                    print("rangt lykilorð")
                    flag=False
                    break
            else:
                print("er ekki í skránni")


    elif val ==4:
        nafn = input("sláðu inn nafn sem þú vilt breyta")
        nafn = nafn.upper()

    elif val ==5:
        on = 0
    else:
        print("þú verður að velja 1-4 og 5 til að hætta")
