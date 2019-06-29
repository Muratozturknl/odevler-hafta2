
print("~"*19,"BURÇMATİK","~"*19)
kaynak="Kaynak: http://www.burclar.net/burclar-tarihleri " 
print(kaynak)
print("~"*len(kaynak),"\n")


    
print(" Doğum Tarih Bilgilerini Giriniz",
      "\nÖrn: mayıs 15 olan tarih için 515","\n")
while True:
    
    tarih=(input("Ay ve günü bitişik yazınızA-GG(çıkış:q): "))
    if tarih=="q":
        break
    
    elif 122 <= int(tarih) <= 219:
        print("  ~Kova~ Burcundasınız!!!\n")

    elif 220 <= int(tarih) <= 320:
        print("  ~Balık~ Burcundasınız!!!\n")
        
    elif 321 <= int(tarih) <= 420:
        print("  ~Koç~ Burcundasınız!!!\n")
        
    elif 421 <= int(tarih) <= 521:
        print("  ~Boğa~ Burcundasınız!!!\n")
        
    elif 522 <= int(tarih) <= 622:
        print("  ~İkizler~ Burcundasınız!!!\n")
        
    elif 623 <= int(tarih) <= 722:
        print("~Yengeç Burcundasınız!!!\n")
        
    elif 723 <= int(tarih) <= 822:
        print("  ~Aslan~ Burcundasınız!!!\n")
        
    elif 823 <= int(tarih) <= 922:
        print("  ~Başak~ Burcundasınız!!!\n")
        
    elif 923 <= int(tarih) <= 1022:
        print("  ~Terazi~ Burcundasınız!!!\n")
        
    elif 1023 <= int(tarih) <= 1121:
        print("  ~Akrep~ Burcundasınız!!!\n")
        
    elif 1122 <= int(tarih) <= 1221:
        print("  ~Yay~ Burcundasınız!!!\n")

    elif int(tarih) > 1222:
        print("  Yanlış giriş yaptınız\n")

    else:
        print("  ~Oğlak~ Burcundasınız!!!\n")
