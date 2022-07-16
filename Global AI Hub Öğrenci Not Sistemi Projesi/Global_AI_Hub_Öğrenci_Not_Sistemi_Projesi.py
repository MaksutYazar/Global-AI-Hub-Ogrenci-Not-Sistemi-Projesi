# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 17:18:56 2022

@author: Maksut
"""
#Globalde Tanýmladýðým deðiþkenler
Ad=[]
Soyad=[]
Numara=[]
Sinav=[]
Harf=[]
Durum=[]
cikis=""
#Listeleri doldurduðumuz döngü
while(True):
    isim =input("Adýnýzý Giriniz: ")
    Ad.append(isim)
    soyisim=input("Soyadýnýzý Giriniz: ")
    Soyad.append(soyisim)
    no=input("Öðrenci Numarasýný Giriniz: ")
    Numara.append(no)
    try:
    Not=int(input("Sýnav Notunu Giriniz: "))
    Sinav.append(Not)
    except ValueError:
        print("Lütfen Sayý giriniz!")
    if Not>84 and Not<=100:
        Harf.append("AA")
        Durum.append("Geçti")
    elif Not>77 and Not<=84 :
        Harf.append("BA")
        Durum.append("Geçti")
    elif Not>70 and Not<=77:
        Harf.append("BB")
        Durum.append("Geçti")
    elif Not>66 and Not<=70:
        Harf.append("CB")
        Durum.append("Geçti")
    elif Not>60 and Not<=66:
        Harf.append("CC")
        Durum.append("Geçti")
    elif Not>55 and Not<=60:
        Harf.append("DC")
        Durum.append("Geçti")
    elif Not >49and Not<=55:
        Harf.append("DD")
        Durum.append("Geçti")
    elif Not>=0 and Not<=49:
        Harf.append("FF")
        Durum.append("Kaldý")
    else:
        print("Yanlýþ giriþ yapýtýnýz!")
    cikis=input("Çýkýþ için 'E' harfini giriniz\nDevam etmek için Enter'a basýnýz: ")
    
    if cikis=="e" or cikis=="E":
        break
#Dateframe yapma, filtreleme ve excel dosyasý
Student={"Ad":Ad,"Soyad":Soyad,"Öðrenci No":Numara,"Sýnav Notu":Sinav,"Harf Notu":Harf,"Durum":Durum}
import pandas as pd 
Dt_Student=pd.DataFrame(Student)
while(True):
    secim=input("Tüm Tabloyu Görmek Ýçin 0 Giriniz\nKalanlarý Görmek Ýçin 1 Giriniz\nGeçenleri Görmek Ýçin 2 Giriniz\nÇýkmak Ýçin 'Q' Giriniz ")
    if secim=="0":
        print(Dt_Student)
    elif secim=="1":
        print(Dt_Student[Dt_Student['Durum'].str.contains("Kaldý")])
    elif secim=="2":
        print(Dt_Student[Dt_Student['Durum'].str.contains("Geçti")])
    elif secim =="q" or secim=="Q":
        break
    else:
        print("Yanlýþ Giriþ Yaptýnýz!")
Dt_Student.to_excel('student.xlsx')
Dt_Student.to_csv('student.csv')
    


















