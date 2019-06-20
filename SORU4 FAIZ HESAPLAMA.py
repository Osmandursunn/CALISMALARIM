print("Faiz Hesaplama Sayfamiza Hosgeldiniz")
anapara=input("Anapara:")
yil=input("Faiz Suresi:")
faiz_orani=input("Faiz Orani:")
toplam_faiz_tutari=float(anapara)*int(yil)*float(faiz_orani)/100
aylik_faiz_tutari=float(toplam_faiz_tutari)/12
gunluk_faiz_tutari=float(toplam_faiz_tutari)/365
toplam_para_miktari=float(anapara)+toplam_faiz_tutari
dosya=open("Faizhesaplama.txt","w")
print("Hesaplanan Faiz Miktari:",toplam_faiz_tutari,"\nAylik:",aylik_faiz_tutari,"\nGunluk:",gunluk_faiz_tutari,"\nToplam:",toplam_para_miktari)
print("Hesaplanan Faiz Miktari:",toplam_faiz_tutari,"\nAylik:",aylik_faiz_tutari,"\nGunluk:",gunluk_faiz_tutari,"\nToplam:",toplam_para_miktari,file=dosya)
dosya.close()
