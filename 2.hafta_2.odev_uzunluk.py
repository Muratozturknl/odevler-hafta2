a="UZAKLIK BİRİM DÖNÜŞTÜRÜCÜ"
print("-"*len(a),"-"*8,sep="")
print("~"*3,a,"~"*3)
print("-"*len(a),"-"*8,sep="")
giriş="""
          (1) Km'yi Mil'e çevirin
          (2) Mil'i Km'ye çevirin
          Çıkmak için 'q' ya basın!
          """
print(giriş)

while True:
    soru=(input("Dönüştürmek istediğiniz birimi seçim: "))

    if soru=="q" :
              print("çıkılıyor...")
              break
              
    elif soru=="1":
                km=float (input("Km: "))
                mil1=1.609344 #km dir.
                print(km,"km", km/mil1, "mil'dir\n")
    elif soru=="2":
                mil=float (input("Mil: "))
                mil1=1.609344 #km dir.

                print(mil,"mil", mil*mil1, "km'dir\n")
