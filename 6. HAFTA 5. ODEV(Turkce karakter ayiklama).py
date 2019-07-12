#Futbolcular dosyasındaki futbolcu isimlerini yazdığınız program ile Türkçe karakter
#içermeyecek bir hale getirip yeni bir dosyaya kaydediniz.

with open("futbolcular.txt") as file:    
  futbolcular=file.read()     
  
kaynak="şçöğüiŞÇÖĞÜİ"  
hedef="scoguiSCOGUI"
tablo=str.maketrans(kaynak,hedef)    

with open("YENİfutbolcular.txt","w") as file:    
  file.write(futbolcular.translate(tablo))   
