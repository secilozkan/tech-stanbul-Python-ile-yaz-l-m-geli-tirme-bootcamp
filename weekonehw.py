"""
#WEEK ONE
#ALIŞTIRMALAR
#soru1
not1=64
not2=86
not3=70
not_ortalama=(not1+not2+not3)/3
print(not_ortalama)

#soru2
ad=input("adınızı giriniz:")
yas=int(input("yaşınızı giriniz:"))
print(ad*yas)

#soru3
import math
r=int(input("yarıçap giriniz:"))
daire_alanı=math.pi*r*r
daire_çevre=2*math.pi*r
print(f"dairenin alanı:{daire_alanı}"
      f"dairenin çevresi:{daire_çevre}")

#soru4
from datetime import date
dogum_yili=int(input("doğum yılınızı giriniz:"))
bu_yil= date.today().year
yas=bu_yil-dogum_yili

if yas>=18:
    print("ehliyet alabilirsiniz")
else:
    print("ehliyet alamazsınız")

#soru5
faiz_oranı=float(input("faiz oranı giriniz:"))
para_miktari=int(input("para miktarı giriniz:"))
print(faiz_oranı*para_miktari*12)

#soru6
kilo=int(input("kilonuzu giriniz:"))
boy=int(input("boyunuzu giriniz:"))
vki= kilo /(boy*boy)
if vki<18.5:
    print("ZAYIF")
elif 18.5<vki<24.9:
    print("NORMAL")
elif 25<vki<29.9:
    print("FAZLA KİLOLU")
else:
    print("OBEZ")

#soru7
ad=input("adınızı giriniz:").lower()
kullanıcı_ad="seçil"
if ad==kullanıcı_ad:
    print("adaşsınız")
else:
    print("adaş değilsiniz")

#soru8
not_ortalama=int(input("not ortalaman:"))
if not_ortalama>85:
    print("TAKTİR")
elif 85>not_ortalama>50:
    print("TEŞEKKÜR")
else:
    print("belge alamazsınız")

#soru9
otoban_uzunluğu=int(input("otoban uzunluğu giriniz:"))
geçiş_süresi=int(input("geçiş süresi giriniz:"))
hız=otoban_uzunluğu/geçiş_süresi
if hız>100:
    print("hız cezası aldınız")

#soru10
yevmiye=350
gun=int(input("çalıştığı gün sayısı:"))
yevmiye_tutarı=yevmiye*gun
print(yevmiye_tutarı)

#KOŞULLU İFADELER
#soru1
memleketim="çanakkale"
memleketin=input("memeleketin:").lower()
if memleketim==memleketin:
    print("hemşiresiniz")
else:
    print("hemşire değilsiniz")
#soru2
sayi1=input("sayı giriniz:")
sayi2=input("sayi giriniz:")
if sayi1<sayi2:
    print(f"{sayi2},{sayi1}")
else:
    print(f"{sayi1},{sayi2}")

#soru3
sayi1=input("sayı giriniz:")
sayi2=input("sayi giriniz:")
sayi3=input("sayi giriniz:")
sayilar=[sayi1,sayi2,sayi3]
sirali=sorted(sayilar,reverse=True)
print(sirali)

#soru4
egitim=input("eğitimiziniz:")
yas=int(input("yasınız:"))
if not egitim=="":
    if 18<=yas:
        print("ehliyet alabilirsiniz")
    else:
        print("ehliyet alamazsınız")
else:
    print("ehliyet alamazsınız")

#question5
while True:
  d=input("will you join the tournament?").lower()
  if d=="agree" or d=="yes":
      print("thank you")
      break
  elif d=="disagree" or d=="no":
      print("sorry")
      break
  else:
      print("Can you repeat it?")

#question6
food=input("food:")
drink=input("drink:")
if not food=="" and drink=="":
    print("the menu is incorrect")
else:
    print("succesfull")

#question7
day=int(input("haftanın hangi günü?"))
if day==1:
    print(f"day {day} neighborhood one")
elif day==2:
    print(f"day {day} neighborhood two")
elif day==3:
    print(f"day {day} neighborhood three")
elif day==4:
    print(f"day {day} neighborhood two")
elif day==5:
    print(f"day {day} neighborhood two")
elif day==6:
    print(f"day {day} neighborhood two")
elif day==7:
    print(f"day {day} neighborhood two")
else:
    print("incorrect entry")

#question8/9
lesson1=int(input("aver:"))
lesson2=int(input("aver:"))
lesson3=int(input("aver:"))
if lesson1>50:
    print("lesson1 pass the course")
else:
    print("lesson1 not pass the course")
if lesson2>50:
    print("lesoon2 pass the course")
else:
    print("lesson2 not pass the course")
if lesson3>50:
    print("lesson3 pass the course")
else:
    print("lesson3 not pass the course")

#question10
user_name=input("please enter your user name?")
password=input("please enter your password!")
x="seçil"
y="ddf233"
if user_name==x and password==y:
    print("You are wellcome!")
else:
    print("Hatalı giriş!")

#question11
mail=input("please enter your mail?")
for i in mail:
    if i=="@" and i==".com":
        print("valid mail!")
    else:
        print("invalid mail")

#question12
programme_language=input("what is your favorite programming language?")
if programme_language=="python":
    print("Guido Rassum\nTim Peters\nBarry Warsaw\nFred l. Drake")
elif programme_language=="java":
    print("James Gosling\nMike Sheridan\nPatrick Naughton\nChris Warth")
elif programme_language=="c++":
    print("Bjarne Stroustrup\nRick Mascitti\nAndrew Koenig\nAlexander Stepanov")
else:
    print("Error!Unknown programming language.")

#question13
user=int(input("Select a menu? One to four"))
if user==1:
    print("32 dollars")
elif user==2:
    print("78 dollars")
elif user ==3:
    print("98 dollars")
elif user ==4:
    print("12 dollars")
else:
    print("Would you choose one of the four menus, please?")

#DÖNGÜLER
#question1
for i in range(31):
    if i%2!=0:
        print(i)

#question2
right=1
add=0
while right<=10:
    number = int(input("number entry:"))
    right+=1
    add+=number
print(add/10)

#question3
for i in range(20,51,3):
    print(i)

#soru4
hak=1
tek_sayi=0
tek_sayim=0
cift_sayi=0
cift_sayim=0
while hak<=20:
    sayi=int(input("sayı giriniz:"))
    hak+=1
    if sayi%2==0:
        cift_sayi+=sayi
        cift_sayim+=1
    else:
        tek_sayi+=sayi
        tek_sayim+=1
print(cift_sayi/cift_sayim)
print(tek_sayi/tek_sayim)

#question5
for i in range(1,11):
    for j in range(1,11):
        print(f"{i}x{j}={i*j}")

#question6
i=1
while i<=10:
     j=1
     while j<=10:
         print(f"{i}x{j}={i*j}")
         j+=1
     i+=1

#question7
while True:
    x = input("enter the password:")
    y = input("enter the password:")
    if x==y:
        print("logged in")
        break
    else:
        print("incorrect entry")

#question8
for i in range(101):
    if i%3==0 and i%5==0:
        print(i)

#question9
for x in range(4):
    print("****")

#question10
x=int(input("horizontal measurement:"))
y=int(input("vertical measurement:"))
for i in range(y):
    print("*"*x)

#question11
satir=int(input("vertical?"))
print('\n...Python Yıldızı...\n')
for i in range(satir):
    print(' '*(satir-i-1) + '*'*(2*i+1))

#question12
for i in range(101):
    print(i)
    if i==35:
        break

#question13
i=int(input("bir sayi giriniz:"))
sayi=0
while True:
    sayi+=1
    print(sayi)
    if sayi==i:
        break

#question14
import random
i=random.randint(1,100)
while True:
    j = int(input("enter a number:"))
    if i==j:
        print("Congratulations,You won!")
        break
    else:
        print("Wrong,Try again!")

#question15
import random
i=random.randint(1,100)
while True:
    j = int(input("enter a number:"))
    if i==j:
        print("Congratulations,You won!")
        break
    elif i>j:
        print("enter larger a number!")
    else:
        print("enter smaller a number!")

#question16
for i in range(1,100):
    if not (i%3==0 and i%5==0):
        print(i)

#soru17
hak=0
toplam=0
while hak<10:
  hak+=1
  sayi=int(input("sayı giriniz:"))
  if sayi%7==0:
      continue
  i=1
  carpım=1
  while i<=sayi:
    carpım *= i
    i+=1
    if sayi<0:
        break
  print(f"{sayi}!={carpım}")
  toplam += carpım
print(toplam)

#question18
num1=int(input("enter a number:"))
num2=int(input("enter a number:"))
ekok=max(num1,num2)
while True:
    if ekok%num1==0 and ekok%num2==0:
        print("ekok=",ekok)
        break
    ekok+=1
ebob=min(num1,num2)
while True:
    if num1%ebob==0 and num2%ebob==0:
        print("ebob=",ebob)
        break
    ebob-=1

#question19
girilen_sayi=input("girilen sayi:")
basamak_sayisi=0
for i in girilen_sayi:
    basamak_sayisi+=1
    if len(girilen_sayi)==basamak_sayisi:
        print(basamak_sayisi)
        break

#question20
sayi=input("bir sayı giriniz:")
us=len(sayi)
toplam=0
for i in sayi:
    toplam+=(int(i)**us)
    if toplam==int(sayi):
        print(f"{sayi},amstrog sayısıdır")
        break
else:
    print("amstrong sayısı değildir")
"""







































