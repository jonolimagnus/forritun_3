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
