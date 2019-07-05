while True:
    try:
        while True:
            pi = 3.14

            print("""
                Islemler:
                A.Alan Hesaplama  
                B.Hacim Hesaplama 
                """)

            islem = input("Lutfen Yapmak Istediginiz Islemi Secin:")

            if islem == "A" or "a":
                print("""
                    Alan Hesaplama Islemleri:
                    1.Kare Alani
                    2.Dikdortgen Alani
                    3.Ucgen Alani
                    """)

                islem = input("Lutfen Alanini Hesaplamak Istediginiz Sekli Secin:")

                if islem == "1":
                    kenar_uzunlugu = int(input("Kenar Uzunlugunu Girin: "))
                    kare_alan = kenar_uzunlugu ** 2
                    print("Karenin Alani:", kare_alan)
                elif islem == "2":
                    kisa_kenar = int(input("Kisa Kenar Uzunlugunu Girin: "))
                    uzun_kenar = int(input("Uzun Kenar Uzunlugunu Girin: "))
                    dikdirtgen_alan = kisa_kenar * uzun_kenar
                    print("Dikdortgenin Alani:", dikdirtgen_alan)
                elif islem == "3":
                    yukseklik = int(input("Ucgenin Yuksekligini Girin: "))
                    taban = int(input("Yuksekligin Ait Oldugu Taban Uzunlugunu Girin: "))
                    ucgen_alan = (yukseklik * taban) / 2
                    print("Ucgenin Alani:", ucgen_alan)
                else:
                    print("Lutfen Gecerli Bir Islem Girin!")
                    continue
            elif islem == "B" or "b":
                print("""
                    Hacim Hesaplama Islemleri:

                    1.Kup Hacmi
                    2.Kure Hacmi
                    3.Koni Hacmi

                    """)

                islem = input("Lutfen Hacmini Hesaplamak Istediginiz Sekli Secin:")

                if islem == "1":
                    kenar_uzunlugu = int(input("Kupun Kenar Uzunlugunu Girin: "))
                    kup_hacim = kenar_uzunlugu ** 3
                    print("Kupun Hacmi:", kup_hacim)
                elif islem == "2":
                    yari_cap = int(input("Kurenin Yaricapini Girin: "))
                    kure_hacim = (4 / 3) * (pi * (yari_cap ** 3))
                    print("Kurenin Hacmi:", kure_hacim)
                elif islem == "3":
                    yukseklik = int(input("Koninin Yuksekligini Girin: "))
                    yari_cap = int(input("Koniye Ait Tabaninin Yaricapini Girin: "))
                    koni_hacim = (1 / 3) * (pi * (yari_cap ** 2)) * yukseklik
                    print("Koninin Hacmi:", koni_hacim)
                else:
                    print("Lutfen Gecerli Bir Islem Girin!")
                    continue
            else:
                print("Lutfen Gecerli Bir Islem Girin!")
                continue
    except:
        print("Hatali Islem!")
        continue
