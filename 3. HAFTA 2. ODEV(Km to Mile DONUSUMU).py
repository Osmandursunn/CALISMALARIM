#Km to Mile/Mil to Km Converter

print("Merhaba")
print("""
Km'yi Mil'e cevirmek icin 1'e
Mil'i-Km'ye cevirmek için 2'ye basiniz
""")
while True:
        seçenek=int(input("""Lütfen yukarıdaki seçeneklerden
dönüşümünü yapmak istediğinizi seçiniz: """))

        quit=input("Programdan Cikmak icin 'q' harfine, devam etmek icin 'ENTER' basiniz")
        if quit=="q":
            print("Sistemden çıkılıyor...")
            break
        pass
        if seçenek ==int(1):
           mil=input("Lütfen dönüşüm yapmak istediğiniz km değerini giriniz: ")
           print(int(mil)*float(0.6213),"mil")
           quit=input("Lütfen sistemden çıkmak için 'q'ya basınız.")
           if quit=="q":
               print("Sistemden çıkılıyor...")
           break
        elif seçenek==int(2):
            km=input("Lütfen dönüşüm yapmak istediğiniz mil değerini giriniz: ")
            print(int(km)*float(1.609),"km")
            quit=input("Lütfen sistemden çıkmak için 'q'ya basınız.")
            if quit=="q":
                print("Sistemden çıkılıyor...")                
            break
        elif quit=="q":
            print("Sistemden çıkılıyor...")
            break
