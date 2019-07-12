#########################  Kullanıcıdan bir input al.##########################


########################## inputtaki rakamların toplamını hesapla########################## 



veri=input("Veri girisi yapiniz:")
sayilar=[]
toplam=0
for i in veri:
    if i in "0987654321":
        sayilar.append(i)
for a in sayilar:
    if a.isdigit()==True:
        toplam+=int(a)
print(toplam)


#farklı karakter girişi de yapabilir
