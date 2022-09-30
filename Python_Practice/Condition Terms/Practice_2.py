
print(" ___İstifadeçi Girişi___\n")

is_ad= "DavudSuleymanov"

is_parol= "123456789"


istifadeci_adi= input("İstifadeci adınızı daxil ediniz..: ")

istifadeci_parol = input ("Parolunuzu daxil ediniz..: ")


if (istifadeci_adi != is_ad and is_parol == istifadeci_parol): 
    
    print("İstifadeçi adınız yanlışdır.. ")

elif (istifadeci_adi == is_ad and is_parol != istifadeci_parol): 

    print("Parolunuz yanlışdır.. ")

elif (istifadeci_adi != is_ad and is_parol != istifadeci_parol): 

    print("İstifadeci adiniz ve parolunuz yanlışdır.. ")

else:
    print(" Girişe nail olundu.. ")













