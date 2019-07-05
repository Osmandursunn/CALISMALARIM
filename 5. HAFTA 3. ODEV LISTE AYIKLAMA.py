#masaustundeki futbolcularin karisik olarak yazildigi txt dosyamizdan cekecegimiz
#futbolculari aktaracagimiz listeleri olusturduk.
galatasaray=[]
fenerbahce=[]
besiktas=[]

futbolcular = open(r"C:\Users\Desktop\futbolcular.txt", "r")
#masaustundeki dosyamiz okunabilir modda

satir_sayisi = 0
with futbolcular as f:
    for line in f:
        satir_sayisi += 1
#dosyamizdaki satir sayisini bulduk (while dongusunde kullanacagiz)

futbolcular = open(r"C:\Users\Desktop\futbolcular.txt", "r")
#dosyamizi tekrar okunur modda actik

a=1
while a<satir_sayisi:
    satir = futbolcular.readline()
    a+=1
    if 'Galatasaray' in satir:
        galatasaray.append(satir)
    elif 'Fenerbahçe' in satir:
        fenerbahce.append(satir)
    elif 'Beşiktaş' in satir:
        besiktas.append(satir)
futbolcular.close()
#while dongusu ile futbolcular.txt dosyamizda satir satir gezerek, futbolculari olusturdugumuz listelere atadik.

galatasaray_txt = open(r"C:\Users\OSMAN\Desktop\galatasaray.txt", "w")
fenerbahce_txt = open(r"C:\Users\OSMAN\Desktop\fenerbahce.txt", "w")
besiktas_txt = open(r"C:\Users\OSMAN\Desktop\besiktas.txt", "w")
#ayirdigimiz futbolculari atayacagimiz(yazdiracagimiz) dosyalari masaustunde olusturduk

a=1
while a<len(galatasaray):
    for i in galatasaray:
        galatasaray_txt.write("{}. {} \n".format(a,i))  # dosyaya yazdik
        a += 1
galatasaray_txt.close()
#galatasaray listesindeki futbolculari while dongusu ile dosyaya aktardik

a=1
while a<len(fenerbahce):
    for i in fenerbahce:
        fenerbahce_txt.write("{}. {} \n".format(a,i))  # dosyaya yazdik
        a += 1
fenerbahce_txt.close()
#fenerbahce listesindeki futbolculari while dongusu ile dosyaya aktardik

a=1
while a<len(besiktas):
    for i in besiktas:
        besiktas_txt.write("{}. {} \n".format(a,i))  # dosyaya yazdik
        a += 1
besiktas_txt.close()
#besiktas listesindeki futbolculari while dongusu ile dosyaya aktardik

print(fenerbahce)
print(galatasaray)
print(besiktas)
