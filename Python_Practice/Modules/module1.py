
def tam_bolunenler (eded):
    
    bolunenler = list()
    
    for i in range (2,eded):
        
        if (eded % i == 0 ):
            
            bolunenler.append(i)
            
    return bolunenler


def ebob_tapma(eded1,eded2):
    
    i = 1
    ebob = 1
    
    while (i <= eded1 and i <= eded2 ): # eded 1= 25
                                        # eded 2= 15

        if ( not (eded1 % i) and not (eded2 % i)):
            
            ebob = i
            
        i += 1
    return ebob












