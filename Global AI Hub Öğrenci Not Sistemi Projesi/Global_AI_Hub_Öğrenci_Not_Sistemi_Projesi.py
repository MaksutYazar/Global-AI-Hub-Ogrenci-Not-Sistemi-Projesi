# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 17:18:56 2022

@author: Maksut
"""
#Globalde Tan�mlad���m de�i�kenler
Ad=[]
Soyad=[]
Numara=[]
Sinav=[]
Harf=[]
Durum=[]
cikis=""
#Listeleri doldurdu�umuz d�ng�
while(True):
    isim =input("Ad�n�z� Giriniz: ")
    Ad.append(isim)
    soyisim=input("Soyad�n�z� Giriniz: ")
    Soyad.append(soyisim)
    no=input("��renci Numaras�n� Giriniz: ")
    Numara.append(no)
    try:
    Not=int(input("S�nav Notunu Giriniz: "))
    Sinav.append(Not)
    except ValueError:
        print("L�tfen Say� giriniz!")
    if Not>84 and Not<=100:
        Harf.append("AA")
        Durum.append("Ge�ti")
    elif Not>77 and Not<=84 :
        Harf.append("BA")
        Durum.append("Ge�ti")
    elif Not>70 and Not<=77:
        Harf.append("BB")
        Durum.append("Ge�ti")
    elif Not>66 and Not<=70:
        Harf.append("CB")
        Durum.append("Ge�ti")
    elif Not>60 and Not<=66:
        Harf.append("CC")
        Durum.append("Ge�ti")
    elif Not>55 and Not<=60:
        Harf.append("DC")
        Durum.append("Ge�ti")
    elif Not >49and Not<=55:
        Harf.append("DD")
        Durum.append("Ge�ti")
    elif Not>=0 and Not<=49:
        Harf.append("FF")
        Durum.append("Kald�")
    else:
        print("Yanl�� giri� yap�t�n�z!")
    cikis=input("��k�� i�in 'E' harfini giriniz\nDevam etmek i�in Enter'a bas�n�z: ")
    
    if cikis=="e" or cikis=="E":
        break
#Dateframe yapma, filtreleme ve excel dosyas�
Student={"Ad":Ad,"Soyad":Soyad,"��renci No":Numara,"S�nav Notu":Sinav,"Harf Notu":Harf,"Durum":Durum}
import pandas as pd 
Dt_Student=pd.DataFrame(Student)
while(True):
    secim=input("T�m Tabloyu G�rmek ��in 0 Giriniz\nKalanlar� G�rmek ��in 1 Giriniz\nGe�enleri G�rmek ��in 2 Giriniz\n��kmak ��in 'Q' Giriniz ")
    if secim=="0":
        print(Dt_Student)
    elif secim=="1":
        print(Dt_Student[Dt_Student['Durum'].str.contains("Kald�")])
    elif secim=="2":
        print(Dt_Student[Dt_Student['Durum'].str.contains("Ge�ti")])
    elif secim =="q" or secim=="Q":
        break
    else:
        print("Yanl�� Giri� Yapt�n�z!")
Dt_Student.to_excel('student.xlsx')
Dt_Student.to_csv('student.csv')
    


















