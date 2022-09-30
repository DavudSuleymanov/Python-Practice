
class Avtomobil(): 
    
    def __init__(self,model,reng,at_gucu,silindir_sayi):
        
        self.model = model
        self.reng = reng 
        self.at_gucu= at_gucu
        self.silindir_sayi = silindir_sayi 
        
avtomobil1= Avtomobil("Mercedec GLS","Qara",250,6)

print("Avtmobil 1 model:",avtomobil1.model)

print("Avtmobil 1 reng:",avtomobil1.reng)

print("Avtmobil 1 at gucu:",avtomobil1.at_gucu)

print("Avtmobil 1 silindir sayi:",avtomobil1.silindir_sayi)


print("--------------------------------------")

avtomobil2= Avtomobil("Bmw", "Qara", 180, 4)

print("Avtmobil 2 model:",avtomobil2.model)

print("Avtmobil 2 reng:",avtomobil2.reng)

print("Avtmobil 2 at gucu:",avtomobil2.at_gucu)

print("Avtmobil 2 silindir sayi:",avtomobil2.silindir_sayi)


print(type("avtomobil1 obyektinin tipi",avtomobil1))

print(type("avtomobil2 obyektinin tipi",avtomobil2))

