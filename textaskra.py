#jón ólafur
#æfingaverk 1C
import math
"""
with open("test.txt","w",encoding="utf-8") as f:
    tala =2
    for x in range(21):
        f.write(str(math.pow(tala,x))+" ")
#búa til skrá
with open("test.txt","r",encoding="utf-8")as f:
    lina =f.readlines()

print(lina)
#lesa skrána
"""

def bua_til_skra():
    with open("test.txt","w",encoding="utf-8")as f:
        tala=2
        for x in range(21):
            f.write(str(math.pow(tala,x))+" ")

#skrifa út skrá
def skrif_ut_skra():
    with open("test.txt","r",encoding="utf-8")as f:
        lina= f.read()
        lina.strip()
        listi=lina.split()
        listi=list(map(float,listi))
        return listi
#aðalforritiðmm
bua_til_skra()#kalla ég í fallið
listi=skrif_ut_skra()
print(listi)
