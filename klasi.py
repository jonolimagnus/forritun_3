#jón ólafur
#verkalýðsfélag

class Verkalydsfelag:
    def __init__(self,nafn,felagsnumer,laun,kennitala):
        self.n=nafn
        self.f=felagsnumer
        self.l=laun
        self.k=kennitala
    def skatt(self):
        return int(self.l) * 0.36#skattur 36%
    def nafn(self):
        return self.n
    def laun(self):
        print("þetta eru laun þeirra", self.l)
    def upplysingar(self):
        return self.n,";",self.f,";",self.l,";",self.k

medlimur1=Verkalydsfelag("jói steinsson",243,300000,"2404786579")
print("skattur",medlimur1.n,medlimur1.skatt(),"kr")

medlimur2=Verkalydsfelag("flóki haldórsson","345",340000,"2306686539")
print("skattur",medlimur2.n,medlimur2.skatt(),"kr")


"""
try:
    with open("verkalydsfelag.csv","w",encoding= "utf-8") as f:
        f.write(Verkalydsfelag)
finally:
    f.close()
"""
