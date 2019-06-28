#Kullanicidan 6 ile 12 karakter araliginda bir parola olusturmasini isteyin.
#Fakat bu parolalarin icerisinde en az birer tane kucuk harf,buyuk harf ve
#rakam olmalidir.'''
# print("Kullanici adi rakam iceremez.")

sayilar=("1234567890")

while True:
    kullanici = input("Username:")
    if len(kullanici)<3 or len(kullanici)>18:
        print("Kullanici adiniz 3 ila 18 karakter arasinda olmalidir.")
        continue

    for a in kullanici:
        if a in sayilar:
            print("Kullanici adi rakam iceremez!!!")
            break
    else:
        break


while True:
    parola = input("Parola belirleyin: ")
    if not parola:
        print("Parola bölümü boş geçilemez!")
    elif len(parola)<6 or len(parola)>12:
        print("parolaniz  6 ila 12 karakter arasinda olmalidir.")
        continue
    else:
        break

print("Username=", kullanici)
print("Parolaniz=",parola)
dosya=open("kullanicibilgiler.txt","w")
print("Username=",kullanici,file=dosya)
print("Parolaniz=",parola,file=dosya)
dosya.close()
