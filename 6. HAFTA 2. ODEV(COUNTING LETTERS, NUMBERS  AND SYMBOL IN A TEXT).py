# Kullanıcıdan bir input alınız.

## Girmiş olduğu inputta

### büyük harf sayısı

#### küçük harf sayısı, rakam sayısı ve bunların haricindeki

##### özel karakter sayılarını veren bir program yazınız


capitals="QWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇ"
sm_lttrs="qwertyuıopğüasdfghjklşizxcvbnmöç"
numbers="0123456789"
capt_letters = ""
small_letters = ""
numberss = ""
symbols = ""

phrase=input("Please write a phrase:")

for i in phrase:
    if i in capitals:
        capt_letters += i
    elif i in sm_lttrs:
        small_letters += i
    elif i in numbers:
        numberss += i
    else:
        symbols += i
print("""There are {} capitals,{} small letters,
{} numbers, and {} symbols in the phrase.
""".format(len(capt_letters),len(small_letters),len(numbers),len(symbols)))
