

  ##   Futbolcular dosyasındaki ismimleri sesli harf ile başlayanları farkli bir dosyaya yazdırınız.  ##

with open("futbolcular.txt") as file:  
  ftb=file.readlines()  


sesliharfler="AEIOUÖÜİaeiouöü" 
for i in ftb:  
  for a in sesliharfler:  

    if i.startswith(a): 
      print(i)    
      with open("seslifutbolcular.txt","a") as dosya:  
        dosya.write(i)  
