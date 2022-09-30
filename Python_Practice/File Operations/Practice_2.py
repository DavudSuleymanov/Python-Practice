fayl = open("Test1.txt","r") # encodig= "utf-8" bu kod ilə faylların oxuma zamanı Azərbaycan dilində hərf gördüyü zaman (ə,ğ.. və.s hərflər kimi ) problem çıxmasın deyə istifadə olunur 

oxu_fayl1= fayl.read()

print("1. Dəfə oxuyuruq\n",oxu_fayl1,sep="")

oxu_fayl2=fayl.read()

print("2. Dəfə oxuyuruq\n",oxu_fayl2,sep="")

fayl.close()


