
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

    def dil_elave_et(self,yeni_dil):
        
        self.diller.append(yeni_dil)
        
        print("Dil Elave Olundu...")
        
    def maas_artir(self,artim_miqdari):
        
        self.maas += artim_miqdari
        
        print("Tebrikler...Maaş artırıldı...")
        
        


proqramist1= Proqramist("Davud", "Suleymanov", 17014908, 100000, ["Python","C","Java"])


proqramist1.informasiya_goster()        


proqramist1.dil_elave_et("C#")        
           
        
proqramist1.informasiya_goster()        


proqramist1.maas_artir(100000)


proqramist1.informasiya_goster()    



















