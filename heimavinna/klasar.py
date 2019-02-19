#jón ólafur
#klasar sýni

class Test():
    "This is my second class"
    a=10
    def func(self):
        print("hello")
class Smiddur():
    def __init__(self,r=0.0):
        self.radius = r
    def ummal(self):
        return round((2*3.14*self.radius),2)
    def flatarmal(self):
        return round(((self.radius*2)*3.14),2)

print(Test.a)
print(Test.__doc__)

ob = Test()#bý til hlut úr klasanum Test
ob2= Test()# hægt er að gera marga hluti úr klasanum
print(ob.a)
print(ob2.__doc__)
print(ob.func)
ob.func()

radius= float(input("sláðu inn radius"))
hlutur = Smiddur(radius)
print("ummál hringsins er =", hlutur.ummal())
print("flatamál hrings er =", hlutur.flatarmal())
