class isciler():
    
    def __init__(self,ad,soyad,no,maas):
        
        self.ad=ad
        self.soyad=soyad
        self.no=no
        self.maas=maas
               
    def informasiya_goster(self):
        print("""
              
              Ad:{}
              Soyad:{}
              No:{}
              Maas:{}
              """.format(self.ad,self.soyad,self.no,self.maas,))
              
class direktorlar(isciler):
    
    def maas_artir(self,zam_miqdari):
        
        print("Maaş artırıldı")
        
        self.maas += zam_miqdari


isci1= isciler("Davud","Suleymanov",17014908,300)

direktor1 = direktorlar("David","Aliyev",18014908,2400)

direktor1.informasiya_goster()

isci1.informasiya_goster()

direktor1.maas_artir(2000)

direktor1.informasiya_goster()

