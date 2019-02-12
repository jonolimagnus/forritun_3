#jón ólafur
#æfingaverkefni try and except

import sys

"""
#prufu verkefni
#halda áfram jafnvel þó að það kemur villa
randomListi =["a",0,2]
for stak in randomListi:
    try:
        print("þetta stak er ", stak)
        r = 1/int(stak)
        break
    except:
        print("Oops!þessi villa kom upp",sys.exc_info()[0])
        print("næsta stak. ")
        print()
print("Tala",stak,"deilt með einum er",r)

#villur
a="b"
try:
    c=int(a)
    #d=23/0
    #f = open("myfile.txt")
    #4 + spam*3
    #"2" +2
except ValueError:
    print("Oops!vitlaus gagnatak",sys.exc_info())
    pass
except (ZeroDivisionError):
    print("Oops!Bannað að deila með núlli",sys.exc_info())
    pass
except (TypeError):
    print("get ekki lagt saman str og int",sys.exc_info())
    pass
except (NameError):
    print("Óskilgreind breyta",sys.exc_info())
    pass
except:
    print("Oops!óvænt villa kom upp",sys.exc_info())
    pass

#villu koði með numerum
try:
    a= int(input("sláðu inn plús tölu samt ekki stærri en hundrað"))
    if a <=0:
        raise ValueError("þetta er ekki plústala")
    if a >100:
        raise ValueError("þessi tala er stærri en 100!")
except ValueError  as x:
    print(x)

#opna og loka srkám
try:
    f = open("test.txt", encoding="utf-8")
    x=f.readline()
    print(x)
    a=int(x)
    x=f.readline()
    print(x)
    a=int(x)
except:
    print("Eitthvað fór úrskeiðis",sys.exc_info())
finally:
    f.close()
print("skránni hefur verið lokuð")


#æfinga verkefninn
#liður 1
listi = []

for x in range(10):
    tala =(input("sláðu inn 10 heiltölur"))
    listi.append(tala)
for stak in listi:
    try:
        print("þetta stak er",stak)
        r=1/int(stak)
        print("Tala",stak,"deilt með einum er",r)
        print()
    except:
        print("Oops!þessi villa kom upp",sys.exc_info()[0])
        print("næsta stak. ")
        print()
"""

#liður2
a="b"
try:
    s=int(a)
    #d=4/0
    #"3" + 4
    #4 +spam*3
    #f=open("myfile.txt")

except ValueError:
    print("Oops!vitlaus gagnatak",sys.exc_info())
    pass
except (ZeroDivisionError):
    print("Oops!Bannað að deila með núlli",sys.exc_info())
    pass
except (TypeError):
    print("get ekki lagt saman str og int",sys.exc_info())
    pass
except (NameError):
    print("Óskilgreind breyta",sys.exc_info())
    pass
except:
    print("Oops!óvænt villa kom upp",sys.exc_info())
    pass

#liður3
try:
    a= int(input("sláðu inn tölu stærri en -10 samt ekki stærri en 200 mátt ekki nota 12"))
    if a <=-10:
        raise ValueError("þessi tala er  minni en -10")
    if a >200:
        raise ValueError("þessi tala er stærri en 200!")
    if a ==12:
        raise ValueError("þessi tala má ekki koma")
except ValueError  as x:
    print(x)

#liður 4
listi = [12,23]
with open("test.txt","w",encoding="utf-8") as f:
    f.write(str(listi))

try:
    f = open("test.txt","r",encoding="utf-8")
    f.read()
    medal =round(sum(listi)/len(listi),1)
    print("þetta er meðaltal listans",medal)
except:
    print("Eitthvað fór úrskeiðis")
finally:
    f.close()
print("skráinn er lokuð")



