
class Proqramist():
    
    def __init__(self,ad,soyad,no,maas,diller):
        
        self.ad= ad
        self.soyad= soyad
        self.no= no 
        self.maas= maas
        self.diller = diller
    
    def informasiya_goster(self): 
        
        print("""
              Proqramist informasiyaları
              
              Ad:{}
              Soyad:{}
              No:{}
              Maas:{}
              Diller:{}
              """.format(self.ad,self.soyad,self.no,self.maas,self.diller))
              
proqramist1= Proqramist("Arif","Qurbanov",17014908,1000,["C++","C#","Python"])
                            
proqramist1.informasiya_goster()

print("--------------------------------------------------------")

proqramist2 = Proqramist("Şehriyar","Mirzeyev",18014908,10000,["C","Python","HTML"])

proqramist2.informasiya_goster()























