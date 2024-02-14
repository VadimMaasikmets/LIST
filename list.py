from random import*
from string import*



#from random import *
#nimed=["Kadri","Mirje","Maadis","Kadri","Linda","Kadri"]
#while True:
#    print("---------------------------------------------------------------------------------------")
#    v=input("N-andmeta näitamine\nL-andmete lisamine\nK-andmete kustutamine\nS-andmete sorteerimine\nE-andmete eemaldamine\nP-andmete pööramine\nC-andmete kopeerimine\nI-indeksi otsing\n").upper()
#    if v=="N":
#        v=input("Kas kõik?(k) või Juhuslik nimi?(j)").lower()
#        if v=="k":
#            print(nimed)
#        elif v=="j":
#            print(choice(nimed))
#    elif v=="L":
#        v=input("Kas lõppu?(l) või positsioonile?(p)").lower()
#        if v=="l":
#            nimi=input("Sisesta nimi: ")
#            nimed.append(nimi)
#        elif v=="p":
#            nimi=input("Sisesta nimi: ")
#            indeks=int(input("Mis positsioonile: "))
#            nimed.insert(indeks-1,nimi)
#    elif v=="K":
#        v=input("Nimi järgi?(n) või järjekorranumbri järgi(j)")
#        if v=="j":
#            while True:
#                try:
#                    indeks=int(input("Mis on järjekorranumber?"))
#                    if 1<=indeks<=len(nimed):
#                        break
#                except ValueError:
#                    print("vale andmetüüp")
#            nimed.pop(indeks-1)
#        elif v=="n":
#            nimi=input("Sisesta nimi: ")
#            mitu=nimed.count(nimi)
#            if mitu>0:
#                for i in range(mitu):
#                    nimed.remove(nimi)
#            else:
#                print(f"{nimi} puudub")
#    elif v=="S":
#        v=int(input("A-z?(1) või Z-a?(2)"))
#        if v==1:
#            nimed.sort()
#        elif v==2:
#            nimed.sort(reverse=True)
#    elif v=="E":
#        nimed.clear()
#        print("Andmed on kustutatud")
#    elif v=="P":
#        print("Oli: ",nimed)
#        nimed.reverse()
#        print("Nüüd: ",nimed)
#    elif v=="C":
#        nimed2=[]
#        print("Oli: " ,nimed2)
#        nimed2=nimed.copy()
#        print("Nüüd: ", nimed2)
#    elif v=="I":
#        nimi=input("Sisesta nimi: ")
#        mitu=nimed.count(nimi)
#        if mitu>0:
#            indeks=0
#            for i in range(mitu):
#                indeks=nimed.index(nimi,indeks+1)
#                print(f"{indeks+1} indeks")
#        else:
#            print(f"{nimi} puudub")





#1
#from string import *


#vokaali=["a","e","i","o","u","õ","ä","ö","ü"]
#konsonanti=["b","d","f","g","h","k","l","m","n","p","r","s","t","š","z","ž","v","w","j"]
#kirjavahemärgid=punctuation
#tühikud=[" "]
#v=0
#r=0
#n=0
#m=0
#tekst=input("Sisestage tekst: ").lower()
#print(tekst)
#tekst_list=list(tekst)
#print(tekst_list)
#for e in tekst_list:
#    if e in vokaali:
#        v+=1
#for e in tekst_list:
#    if e in konsonanti:
#        r+=1
#for e in tekst_list:
#    if e in kirjavahemärgid:
#        n+=1
#for e in tekst_list:
#    if e in tühikud:
#        m+=1
#print(f"Vokaali: {v} ja  Konsonanti: {r} ja kirjavahemärgid {n} ja tühikud {m}")




##2
#nimed=[]
#for i in range(5):
#    nimi=input("Sisesta nimi: ")
#    nimed.append(nimi)
#print("Sisestatud: ", nimed)
#nimed.sort()
#print("Sorteeritud: ", nimed)
#print("Vimasena oli lisatud: ", nimi)
#nimi=input("Mis nimi on vaja asendada? ")
#indeks=nimed.index(nimi)
#uus_nimi=input("Uus nimi: ")
#nimed[indeks]=uus_nimi
#õpilased=["Juhan","Kati","Mario","Mario","Mati","Mati"]
#uus_list=list(set(õpilased))
#print(õpilased, "Vana loetelu")
#uus_list.sort()
#print(uus_list, "Uus loetelu")
#vanused=[]
#for i in range(5):
#    v=int(input("Sisesta vanus: "))
#    vanused.append(v)
#sum_=sum(vanused)
#min_=min(vanused)
#max_=max(vanused)
#kesk=sum_/len(vanused)
#print("Keskmine on {kesk}, \nSuurim on {max_}, \nVäiksem on {min_}, \nSumma on {sum_}")


##3
#from random import*
#from string import*
#while True:
#    try:
#        N=int(input("Mitu rida loome?"))
#        break
#    except:
#        print("Vale tüüp")
#while True:
#    try:
#        S=input("Mis sümbol korrutame?")
#        if S in punctuation:
#            break
#        else:
#            print("Vale sümbol")
#    except:
#        print("Vale sümbol")
#for i in range(N):
#    print(randint(1, 25)*S)



##4
#Indeksid=["Tallinn","Narva","Kohtla-Järve","Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","Tartu","Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa,Harjumaa, Raplamaa","Pärnumaa","Läänemaa, Hiiumaa, Saaremaa"]
#while True:
#    indeks=input("Indeks: ")
#    if len(indeks)==5 and indeks.isdigit()==True and indeks[0]!="0":  #int(indeks[0])!=0
#        print("Sa elad piirkonnas", Indeksid[int(indeks[0])-1])
#        if indeks[0]=="1" or indeks[0]=="2" or indeks[0]=="3":
#            print("Stay Home!!!!!!!!")
#        else:
#            print("Kanna maski, kurat!!!!")
#        break
#    else:
#        print("Vale indeks, sisestage uuesti: ")



##5
#rida=[]
#N=randint(2,25)
#for i in range(N):
#    rida.append(choice(ascii_uppercase))
#print(rida)
#n=(input("Mitu paari vahetada "))
#if len(rida)//2>n:
#    for i in range(n):
#        abi=rida[i]
#        rida[i]=rida[len(rida)-1-i]
#        rida[len(rida)-1-i]=abi
#else:
#    print("liiva vähe elemente")
#print(rida)



##6
#arvud=[1,2,3,4,5,6,122,44,5]
#print(arvud)
#max_=max(arvud)
#indeks=arvud.index(max_)
#max_=int(max_/len(arvud))
#arvud[indeks]=max_
#print(arvud)



##9 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!САМОСТОЯТЕЛЬНО!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#glas=["a","e","i","o","u","õ","ä","ö","ü"]
#sogl=["b","d","f","g","h","j","k","l","m","n","p","r","s","š","z","ž","t","v"]
#while True:
#    name=input("Sisesta nimi: ")
#    try:
#        if name.isalpha(): #метод проверки есть ли ТОЛЬКО буквы в строке
#            namelenght=len(name)
#            glascount=sum(name.count(symbol) for symbol in glas) #задал переменную для представления отдельного символа в строке
#            soglcount=sum(name.count(symbol) for symbol in sogl)
#            unique=sorted(set(name))# использую множество set для хранения уникальных букв имени в функицю sorted() 
#            print("Privet, " + name.capitalize() + "!") #Для преобразования первого символа строки в заглавную
#            print("Koli4estvo bukv v imeni: ", namelenght)
#            print("Koli4estvo glasnih: ", glascount)
#            print("Koli4estvo soglasnih: ", soglcount)
#            print("Bukvq vashego imeni v alfavitnom porjadke: ")
#            for symbol in unique:
#                print(symbol, end=" ")
#            print()

#            break
#        else:
#            print("Pozaluista, ispolzujte tolko bukvq.")
#    except:
#        ValueError


##12
#import random
#number=[random.randint(1,100) for _ in range(10)] #использую нижнее подчеркивание в качестве временной переменной
#print("Ishodnqi kod: ", number)
#min_=number.index(min(number))
#max_=number.index(max(number))
##меняем местами
#number[min_], number[max_]=number[max_], number[min_]
#print("Spisok posle zamenq minimalnogo i maksimalnogo: ", number)