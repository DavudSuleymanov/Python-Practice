

print("""--------------------------------------
          Kalklytor Programına Xoş Gelmisiniz
          
          Prosesler:
              
              1- Toplama
              2- Çıxma
              3- Vurma
              4- Bölme
          --------------------------------------     
      """)


a= int (input("İlk reqemi daxil ediniz.."))

b= int (input("İkinci reqemi daxil ediniz.."))

proses= int(input("İcra etmek istediyiniz proses kodunu daxil ediniz.."))



if (proses==1): 
    
    print("{} ile {}'nin toplamı {}-a beraberdir".format(a,b,a+b))

elif (proses==2):
    
    print("{} ile {}'nun ferqi {}-a beraberdir".format(a,b,a-b))

elif (proses==3):
    
    print("{} ile {}'nun vurumu {}-a beraberdir".format(a,b,a*b))


elif (proses==4):
    
    print("{} ile {}'nun bölümü {}-a beraberdir".format(a,b,a/b))
    
else:
    print("Bele bir proses kodu yoxdur.. ")










