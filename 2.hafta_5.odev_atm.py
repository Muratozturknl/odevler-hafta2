a=" §-SANAL BANK SANAL ATM'YE-§"
print(*a,"\n",*("~"*len(a)))

bakiye=1000

while True:
    soru=(input("Lütfen yapmak istediğiniz işlemi seçiniz!\n"
                "(1) Bakiye Sorgulama (2) Para Çekme (3) Para Yatırma (4) İptal \nİşlem numarası...:"))
    
    if soru=="4" :
              print("Lütfen kartınızı almayı unutmayınız...")
              break
              
    elif soru=="1":
        print("Bakiyeniz: ","~",bakiye,"~","\n",sep="")
              
    elif soru=="2":
        miktar=float(input("Miktar: "))
        if miktar >bakiye:
            print("İşleminiz için bakiyeniz yetersizdir!!!")
        else:
            bakiye-=miktar
            print("İşleminiz neticesinde bakiyeniz: ","~",bakiye,"~","\n",sep="")
            
    elif soru=="3":
        miktar=float(input("Miktar: "))
        bakiye+=miktar
        print("İşleminiz neticesinde bakiyeniz: ","~",bakiye,"~","\n",sep="")
      
    else:
           print("\nSeçim yapmadınız ve ya yanlış giriş yaptınız!\n")
    




