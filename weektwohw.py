"""
#WEEK TWO
#KOLEKSİYONLAR
#question1
menu=[{"drinks":["lemonade","tea","coffee"]},
      {"desserts":["cake","magnolia","ice cream"]},
      {"soups":["lentil","tripe","vermicelli"]}]
#question2 and question3
menu={"drinks":{"lemonade":12,
                 "tea":13,
                 "coffee":14},
      "desserts":{"cake":15,
                   "magnolia":16,
                   "ice cream":18},
      "soups":{"lentil":19,
                "tripe":20,
                "vermicelli":21
                }}
for kategori,yemekler in menu.items():
    print(f"\nKategori:{kategori}")
    for i,(yemek,fiyat) in enumerate(yemekler.items(),1):
        print(f"\n{i}.{yemek}:{fiyat}")
my_menu=[]
x=input("içecek seçin")
my_menu.append(x)
y=input("tatlı seçin")
my_menu.append(y)
z=input("çorba seçin")
my_menu.append(z)
print("MENÜM")
for i in range(1,len(my_menu)+1):
    print(f"{i}.{my_menu[i-1]}")

print(int(menu["drinks"][x])+int(menu["desserts"][y])+int(menu["soups"][z]))

#question4
print("MY CV")
name=input("adınızı giriniz:")
surname=input("soyadınızı giriniz:")
lessons={}
while True:
    lesson = input("ders giriniz")
    if lesson.lower()=="bitti":
         break

    Not=int(input("not giriniz"))
    lessons[lesson]=Not
print(f"ad:{name}\nsoyad:{surname}")
print("Lessons")
for lesson,Not in lessons.items():
    print(f"-{lesson}:{Not}")

#question5
todo=[]
while True:
    task=input("yapmanız gerekenler")
    if task.lower()=="tamam":
        break
    todo.append(task)
for i,task in enumerate(todo,1):
    while True:
     print(f"{i}.{task}")
     j=input("yapıldı mı yes/no")
     if j=="yes":
        break
print("thank you")

#question6 and question7
todo={}
while True:
    kategori=input("hangi kategori")
    if kategori.lower()=="show todo":
        break
    alt_kategori=[]
    while True:
        gorev=input("görev girin")
        if gorev.lower()=="yeni kategori":
            break
        alt_kategori.append(gorev)
    todo[kategori]=alt_kategori
print("yapılacaklar listesi")
for kategori,gorev in todo.items():
    print(f"\nkategori:{kategori}")
    for gorev in alt_kategori:
        print(f"-{gorev}")

#question8
liste=[]
while True:
   sayi=input("sayı giriniz:")
   if sayi.upper()=="OK":
       break
   liste.append(int(sayi))
sag=liste[len(liste)//2:]#divide
sol=liste[:len(liste)//2]
for i in range(len(sag)-1):
    if sag[i]>sag[i+1]:
        sag[i],sag[i+1]=sag[i+1],sag[i]
for j in range(len(sol)-1):
    if sol[j]>sol[j+1]:
        sol[j],sol[j+1]=sol[j+1],sol[j]
print(sag)
print(sol)
if sag[0]<sol[0]:#conquer
    print(f"en küçük sayı:{sag[0]}")
else:
    print(f"en küçük sayı:{sol[0]}")
if sag[len(sag)-1]>sol[len(sol)-1]:
    print(f"en büyük sayı:{sag[len(sag)-1]}")
else:
    print(f"en büyük sayı:{sol[len(sol)-1]}")

#question9
liste = []
while len(liste)<6:
   sayi=int(input("6 tane sayı giriniz:"))
   liste.append(sayi)
print("girilen sayılar:",liste)
sayilan=[]
while liste:
    i=liste[0]
    if i not in sayilan:
      sayac = 0
      for j in liste:
          if i==j:
            sayac+=1
      print(f"{i}:{sayac}")
      sayilan.append(i)
    liste.pop(0)

#question10
dict={}
while True:
    yazar=input("en sevdiğin yazar")
    if yazar.lower()=="bitti":
        break
    eserler = []
    while True:
        eser = input("en sevdiğin eserleri")
        if eser.lower()=="yok":
            break
        eserler.append(eser)
        dict[yazar] = eserler
for sira,(yazar,eserler) in enumerate(dict.items(),1):
   print(f"\n{sira}.{yazar}")
   for i in eserler:
       print("-",i)

#question11
asal_sayilar=[]
for i in range(2,1001):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        asal_sayilar.append(i)
print(f"asallar:{asal_sayilar}")
"""
æ





