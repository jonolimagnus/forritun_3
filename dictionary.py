#jón ólafur
#æfingaverkefni 1B
import random
#liður 1
safn ={"A":"api","B":"banani","C":"cookies","D":"dreki","E":"epli","F":"franskar","G":"grautur","H":"hrafn",}#bý til dictonary
#liður 2
for k,v in safn.items():
    print(k,"er fyrir",v)#skrifa út listan
#liður 3
print()
print(safn["E"])#prenta út E
#liður 4
print()
safn["H"]="haf"#breytti H úr hafni í haf
#liður 5
print(safn)
#liður 6
print()
del safn["C"]#eyðir C úrt dictionary
#liður 7
for k,v in safn.items():
    print(k,"er fyrir",v)
#print(safn)
#liður 8
print()
print(safn.popitem())#eyðir aftasta stakinu
#liður 9
for k,v in safn.items():
    print(k,"er fyrir",v)
#print(safn)
#liður 10
safn2 = safn.copy()#bætti við safn 2
safn2["C"]="cookies"
print("afrit af safn")
for k,v in safn2.items():
    print(k,"er fyrir",v)
print("gamal safnið")
for k,v in safn.items():
    print(k,"er fyrir",v)
#liður 11
del safn2#eyði safni2
#liður 12
"""
for k,v in safn2.items():
    print(k,"er fyrir",v)
"""
#ef ég nota þennan kóða fæ ég villu
#liður 13
print()
tolur={}#bý til dictonary með key frá 1 til 5 með random tölum sem value frá 100-1000
for x in range(1,6):
    tolur[x] = random.randint(100,1000)
print(tolur)
#liður 14
print()
for k,v in tolur.items():
    print(k,"er fyrir",v)
#sýni aðferðinn með items
print()
test = {1: "matur",2: "skóli",3: "bíl"}
print(test.keys())
#sýni aðferðina með keys
print()
print(test.values())
#nota aðferðina með values
print()
print(test)
test.clear()
#not aðferðina clear
print(test)
