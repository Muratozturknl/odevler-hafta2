giriş=("""
!!-Kullanıcı adı ve şifre oluşturma programına hoşgeldiniz-!!
~~~» Kullanıcı adınız en az 3 en fazla 18 karakterden,
şifreniz ise en az 6 en fazla 12 karakterden oluşmalıdır.
İşlemleri sonlandırmak için q ye basınız. «~~~
""")
print(giriş)
anahtar=1
while anahtar==1:
        user=input("Kullanıcı adı giriniz:")
        if user=="q":
            print("Programdan çıkmak için tekrar q'ya basınız!")
            anahtar=0

        elif "0" in user or "1" in user or "2" in user or "3" in user or "4" in user or "5" in user or "6" in user or"7" in user or "8" in user or "9" in user:
                print('"Kullanıcı adı ~rakam~ içermemeli,lütfen tekrar deneyiniz!"')

        elif len(user) <= 2 :
           print("~3~ Karakterden az giriş yaptınız!")

        elif len(user) >= 19:
            print("~18~ karakterden fazla giriş yaptınız!")


        else:
            print("Kullanıcı adınız:",user)
            break  
#----------------------------------------------------------------------------------------------
anahtar1=1
while anahtar1==1:
    şifre=input("Lütfen şifre giriniz:")
    şifre_len=len(şifre)
    if şifre =="q":
        print("Programdan çıkılıyor!")
        anahtar1=0
        continue    
          
    elif şifre_len<= 5:
          print("6 Karakterden az giriş yaptınız!")
          continue

    elif şifre_len >= 13:
          print("12 karakterden fazla giriş yaptınız!")
          continue
    else:
          print("Şifreniz:",şifre)
          
    
    print("Kullanıcı adınız....: ",user,"\n","Şifreniz............: ",şifre, sep="")
    
    dosya=open("parolakontrol.txt","w")
    print("Kullanıcı adınız....: ",user,"\n","Şifreniz............: ",şifre, sep="",file=dosya)
    dosya.close()
    break

