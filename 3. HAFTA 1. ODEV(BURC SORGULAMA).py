#Burc Hesaplama Projesi(Basit)


print("Burc Sorgulama Ekranina Hosgeldiniz\nLutfen Dogum Gunu Bilgilerinizi Giriniz:")

a=int(input("Lutfen Dogdugunuz Gunu Sayi Olarak Giriniz:"))
b=int(input("Lutfen Dogdugunuz Ayi Sayi olarak giriniz:"))

if ((a>20)&(b==3)) or ((a<21)&(b==4)):
    y="Koc"
elif((a>20)&(b==4)) or ((a<22)&(b==5)):
    y="Boga"
elif((a>21)&(b==5)) or ((a<23)&(b==6)):
    y="ikizler"
elif((a>22)&(b==6)) or ((a<23)&(b==7)):
    y="Yengec"
elif((a>22)&(b==7)) or ((a<23)&(b==8)):
    y="Aslan"
elif((a>22)&(b==8)) or ((a<23)&(b==9)):
    y="Basak"
elif((a>22)&(b==9)) or ((a<23)&(b==10)):
    y="Terazi"
elif((a>22)&(b==10)) or ((a<22)&(b==11)):
     y="Akrep"
elif((a>21)&(b==11)) or ((a<22)&(b==12)):
     y="Yay"
elif((a>21)&(b==12)) or ((a<22)&(b==1)):
     y="Oglak"
elif((a>21)&(b==1)) or ((a<20)&(b==2)):
     y="Kova"
else:
     y="Balik"
     
print("Burcunuz:",y)

