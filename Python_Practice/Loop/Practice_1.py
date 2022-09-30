


print("""
      
      Faktorial Tapma Proqramı 
      
          Proqramdan çıxmaq istesiniz "q" ya basın.\n
          
      """)


while True :
    
    reqem = input("\nReqemi daxil ediniz..: ")
    
    if(reqem=="q"):
        
        print("Proqramdan çıxılır")
        
        break
    
    reqem= int(reqem)

    fakt=1
    
    # range(1,10)
    
    
    for i in range(2,reqem+1):
        
        fakt *= i # fakt= fakt *i 

    print("Faktoriyel:",fakt)









