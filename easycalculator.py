# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def toplama(x,y):
    return(x+y)

def cikarma(x,y):
    return(x-y)

def carpma(x,y):
    return(x*y)

def bolme(x,y):
    return(x/y)

print("--------BASİT HESAP MAKİNESİNE HOŞ GELDİNİZ---------")
print("By Asrın Haktan")


while True:
    print("çıkmak için q'ya basınız.")
    secim = str(input("Yapmak istediğiniz işlemi seçiniz:\n 1-toplama\n 2-çıkarma\n 3-çarpma\n 4-bölme\n Seçiminiz : "))
    if secim == "q":
        print("çıkış yapılıyor...")
        break
    ilksayi = float(input("işlem yapılacak ilk sayıyı giriniz : "))
    ikincisayi = float(input("işlem yapılacak ikinci sayıyı giriniz : "))
    

    
    if secim == "1":
       print("işlem sonucunuz:",toplama(ilksayi,ikincisayi))
       continue
    elif secim == "2":
        print("işlem sonucunuz:",cikarma(ilksayi,ikincisayi))
        continue
    elif secim == "3":
        print("işlem sonucunuz:",carpma(ilksayi,ikincisayi))
        continue
    elif secim == "4":
        print("işlem sonucunuz:",bolme(ilksayi,ikincisayi))
        continue
    
    else:
        print("hatalı giriş yaptınız tekrar deneyiniz")
        continue

 
    
    
    
    
    
    
    