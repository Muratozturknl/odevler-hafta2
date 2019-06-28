
print("~"*19,"BURÇMATİK","~"*19)
kaynak="Kaynak: http://www.burclar.net/burclar-tarihleri " 
print(kaynak)
print("~"*len(kaynak),"\n")


    
print(" Doğum Tarih Bilgilerini Giriniz",
      "\nÖrn: mayıs 15 olan tarih için 515","\n")


tarih=int(input("Ay ve günü bitişik yazınız: "))

if 122 <= tarih <= 219:
    print("  ~Kova~ Burcundasınız!!!\n")

elif 220 <= tarih <= 320:
    print("  ~Balık~ Burcundasınız!!!\n")
    
elif 321 <= tarih <= 420:
    print("  ~Koç~ Burcundasınız!!!\n")
    
elif 421 <= tarih <= 521:
    print("  ~Boğa~ Burcundasınız!!!\n")
    
elif 522 <= tarih <= 622:
    print("  ~İkizler~ Burcundasınız!!!\n")
    
elif 623 <= tarih <= 722:
    print("~Yengeç Burcundasınız!!!\n")
    
elif 723 <= tarih <= 822:
    print("  ~Aslan~ Burcundasınız!!!\n")
    
elif 823 <= tarih <= 922:
    print("  ~Başak~ Burcundasınız!!!\n")
    
elif 923 <= tarih <= 1022:
    print("  ~Terazi~ Burcundasınız!!!\n")
    
elif 1023 <= tarih <= 1121:
    print("  ~Akrep~ Burcundasınız!!!\n")
    
elif 1122 <= tarih <= 1221:
    print("  ~Yay~ Burcundasınız!!!\n")

else:
    print("  ~Oğlak~ Burcundasınız!!!\n")
