değer=0
sayi=input("Sayiniz:")
for i in range(2,int(sayi)):
      if(int(sayi)%i==0):
            değer+=1
            break
if(değer!=0):
      print(sayi,"Sayiniz Asal Değildir.")
else:
      print(sayi,"Sayiniz Asal Sayidir.")

