#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 20:57:10 2020

@author: asrinhaktansahin
"""

class Aritmetik():

    def _init_(self):
        pass

    def toplama(self, deger1, deger2):
        sonuc = deger1 + deger2
        return sonuc

    def cikarma(self, deger1, deger2):
        sonuc = deger1 - deger2
        return sonuc

    def bolme(self, deger1, deger2):
        sonuc = deger1 / deger2
        return sonuc

    def carpma(self, deger1, deger2):
        sonuc = deger1 * deger2
        return sonuc

    def moduler_bolme(self, deger1, deger2):
        sonuc = deger1 % deger2
        return sonuc

    def tamsayi_bolme(self, deger1, deger2):
        sonuc = deger1 // deger2
        return sonuc


class Dizi(Aritmetik):
    def _init_(self):
        Aritmetik._init_(self)

    def fibonacci(self, deger):
        n1, n2 = 0, 1
        sayac = 0
        sonuc = []

        # check if the number of terms is valid
        if deger <= 0:
            print("Pozitif sayi giriniz")
        elif deger == 1:
            print("Fibonacci degeri ", deger, "'den buyuk olmali")
            print(n1)
        else:
            while sayac < deger:
                sonuc.append(n1)
                nth = n1 + n2
                n1 = n2
                n2 = nth
                sayac += 1
            return sonuc

    # Asiri yukleme (Overload)
    def asal_sayilar(self, deger1, deger2=None):
        sonuc = []

        if (deger2 == None):
            deger2 = deger1
            deger1 = 0

        for sayi in range(0 if deger2 == None else deger1, deger2 + 1):
            if sayi > 1:
                for i in range(2, sayi):
                    if (sayi % i) == 0:
                        break
                else:
                    sonuc.append(sayi)
        return sonuc

    # Metot ezme (Override)
    def toplama(self, *deger):
        sonuc = 0
        for i in deger:
            sonuc += i
        return sonuc


aritmetik = Aritmetik()
dizi = Dizi()

print("Aritmetik toplama: 5 + 5", aritmetik.toplama(5, 5))
print("Aritmetik cikarma: 10 - 5", aritmetik.cikarma(10, 5))
print("Aritmetik carpma: 5 * 5", aritmetik.carpma(5, 5))
print("Aritmetik bolme: 5 / 3", aritmetik.bolme(5.0, 3.0))
print("Aritmetik mod: 5 % 2", aritmetik.moduler_bolme(5, 2))
print("Aritmetik tamsayi bolme: 5 / 3", aritmetik.tamsayi_bolme(5, 3))

print("\n")

print("Dizi fibonacci: 10", dizi.fibonacci(10))
print("Dizi asal sayilar: 10", dizi.asal_sayilar(10))
print("Dizi asal sayilar: 10-20", dizi.asal_sayilar(10, 20))
print("Dizi toplama: 3, 4, 5", dizi.toplama(3, 4, 5))