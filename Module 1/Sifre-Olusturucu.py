import random


krkt = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
print("--------------------------------------------ŞİFRE OLUŞTURUCU-----------------------------------------------------------")
print("                                                                                                                       ")
uzunluk = int(input("                                      Şifre ne kadar uzun olsun: "))
print("                                                                                                                       ")

parola = ""

for i in range(uzunluk):
    karakter = random.choice(krkt)
    parola += karakter

print("                                      Parolanız: ", parola)
print("                                                                                                                       ")
print("-----------------------------------------------------------------------------------------------------------------------")