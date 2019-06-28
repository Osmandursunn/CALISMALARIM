print("Lutfen Yapmak Istediginiz Islemi Tuslayiniz:")
print("1)Bakiye kontrolu icin 1'yi\n2)Para Yatirmak icin 2'i\n3)Para Cekmek Icin 3'u tuslayin")

bakiye=1000
while True:
    islem = int(input("Isleminizi Tuslayin:"))
    if islem==1:
        print("Toplam Bakiyeniz:",bakiye,"Euro'dur.")
        cevap = input("Baska Bir islem yapmak ister misiniz? E/H")
        if cevap == "e" or cevap == "E":
            continue
        elif cevap=="h"or cevap=="H":
            print("Sistemden Cikiliyor...")
            break
        else:
            print("Hatali Giris yapriniz!")

    elif islem==2:
        para_yatirma=int(input("Yatircaginiz tutari Giriniz:",))
        yeni_bakiye=bakiye+para_yatirma
        bakiye=yeni_bakiye
        print("Yeni Bakiyeniz:",yeni_bakiye,"Euro'dur.")
        cevap=input("Baska Bir islem yapmak ister misiniz? E/H")
        if cevap == "e" or cevap == "E":
            continue
        elif cevap=="h"or cevap=="H":
            print("Sistemden Cikiliyor...")
            break
        else:
            print("Hatali Giris yaptiniz!")

    elif islem==3:
        cekilen=int(input("Cekmek istediginiz Tutari Giriniz:"))
        if cekilen>bakiye:
            print("Yetersiz Bakiye!")

        else:
            kalan=bakiye-cekilen
            bakiye=kalan
            print("Kalan Bakiye:",kalan,"Euro'dur.")
            cevap = input("Baska Bir islem yapmak ister misiniz? E/H")
            if cevap == "e" or cevap == "E":
                continue
            elif cevap == "h" or cevap == "H":
                print("Sistemden Cikiliyor...")
                break
            else:
                print("Hatali Giris yaptiniz!")

    else:
        print("Gecersiz bir giris yaptiniz! Lutfen tekrar deneyiniz.")
        break
