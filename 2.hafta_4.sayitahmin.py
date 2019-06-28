
print("---------- Sayı tahmin oyununa hoşgeldiniz! ----------")
print("\t1 ila 10 arasında bir sayı tahmin ediniz")

tahmin=1

for i in range(5):
    print(i+1,". deneme",sep="")
    sayı=input("Lütfen bir sayı tahmin ediniz:")

   
    # 1 denemede...
    if i == 0 and int(sayı) == tahmin:
        print ("Tahmininiz doğru, tebrikler * * * kazandınız!!")
        break

    #2 yada 3 denemede
    elif 1<= i <= 3  and int(sayı) == tahmin:
        print ("Tahmininiz doğru, tebrikler * * kazandınız!!")
        break

    #4 yada 5 denemede
    elif 4 <= i <= 5  and int(sayı) == tahmin:
        print ("Tahmininiz doğru, tebrikler  * kazandınız!!")
        break
  
    
    else:
            print("Kaybetiniz!")
        
