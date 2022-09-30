# Sade Ədədlər: Yalnız birə və özünə bölünən ədədlər sadə ədədlərdir: 2, 3, 11, 29, 101 və s.


def sade_eded(eded): 
    if (eded==1):
        return False
    elif (eded==2):
        return False 
    else: 
        for i in range (2,eded):
            if (eded % i == 0):
                return False
            
        return True     
        
        
while True: 
    
    eded= input("Yoxlamaq istediyiniz ededi daxil ediniz: ")
    
    if (eded=="q"): 
        break
    else: 
        eded = int (eded)
        
        if (sade_eded(eded)):
            
            print("Daxil etmiş olduğunuz {} ededi sade ededdir".format(eded))
        
        else: 
            print("Daxil etmiş olduğunuz {} ededi sade eded deyildir".format(eded))
        
        
        
        
        
        
        