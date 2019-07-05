print("sayı tahmin oyununa hoş geldiniz...")
sayı=75
sefer=0
try:
    while sefer<=100:
        tahmin=int(input("lütfen 0 ile 100 arasında bir sayı tahmin ediniz:"))
        sefer+=1
        fark=sayı-tahmin
        tfark=tahmin-sayı
        if sayı!=tahmin:
            if fark>0:
                if 0<fark<10:
                    print("çok yaklaştın biraz daha çıkmalısın")
                    continue
                elif 10<fark<30:
                    print("daha yüksek bir sayı girmelisin")
                    continue
                elif 30<fark<70:
                    print("çok daha yüksek bir sayı girmelisin")
                    continue
                else:
                    print("arada dağlar kadar fark var epey çıkmalısın")
                    continue
            if tfark>0:
                if 0<tfark<10:
                    print("çok yaklaştın biraz daha inmelisin")
                    continue
                elif 10<tfark<30:
                    print("daha düşük bir sayı girmelisin")
                    continue
                elif 30<tfark<70:
                    print("çok daha düşük bir sayı girmelisin")
                    continue
                else:
                    print("arada dağlar kadar fark var çok inmrlisin")
                    continue
        if sayı==tahmin:
            print("tebrikler sayıyı {}. denemede bildiniz".format(sefer))
            break
except:
    print("hatalı giriş yaptınız")
