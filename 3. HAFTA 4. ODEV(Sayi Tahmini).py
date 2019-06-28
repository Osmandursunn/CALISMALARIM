#Sayi
#Tahmini

print("""1 ile 10 arasi bir rakam var aklimda. Haydi tahmin et """)

sayi=2
for i in range(8):
    tahmin=int(input("1-10 arası bır sayı yazınız:  "))
    if (i==4 or i==3) and sayi==tahmin:
        print("Sanki biraz zorlandin...")
        print("*")
        break
    elif (i==2 or i==1) and sayi==tahmin:
        print("Iyi yoldasin...")
        print("**")
        break
    elif i==0 and sayi==tahmin:
        print("Tebrikler...")
        print("***")
        break
    elif i==5:
        print("Bilemediniz!!!")
        break
