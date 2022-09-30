with open("Test1.txt","r") as fayl: 
    
    print("Kursorumuz bu baytdadır",fayl.tell())
    
    fayl.seek(34)
    
    print("Kursorumuz bu baytdadır",fayl.tell())
    
    oxu_fayl= fayl.read()
    
    print("Faylın içindeki deyer: ", oxu_fayl) 