# fájl beolvasása
f = open("ki.txt", "r", encoding="utf8")
lines = f.readlines()

f.close()

lista = []
szam = []
szoveg=[]

# eldönti hogy szöveg vagy szám van a fájlban
for line in lines:
    for elem in line.split(";"):
        if elem.isdigit():
            szam.append(int(elem))
        elif elem.isalpha():
            szoveg.append(elem)

if szam and not szoveg:
    print("A fájl csak számokat tartalmaz.")
elif szoveg and not szam:
    print("A fájl csak betűket tartalmaz.")
else:
    print("A fájl vegyesen tartalmaz számokat és betűket, vagy pedig helyetelen az adat.")
   
# buborékrendezés
if szam:
    irany = input("A buborékrendezés növekvő vagy csökkenő sorrendben történjen? ")

   
    for i in range(len(szam) - 1):
        for j in range(len(szam) - 1 - i):
            if irany == 'növekvő':  
                if szam[j] > szam[j + 1]:
                    szam[j], szam[j + 1] = szam[j + 1], szam[j]
            elif irany == 'csökkenő':  
                if szam[j] < szam[j + 1]:
                    szam[j], szam[j + 1] = szam[j + 1], szam[j]

    print(f"Buborékrendezés számokkal: {szam}")


if szoveg:
    irany = input("A buborékrendezés növekvő vagy csökkenő sorrendben történjen? ")

   
    for i in range(len(szoveg) - 1):
        for j in range(len(szoveg) - 1 - i):
            if irany == 'növekvő':  
                if szoveg[j] > szoveg[j + 1]:
                    szoveg[j], szoveg[j + 1] = szoveg[j + 1], szoveg[j]
            elif irany == 'csökkenő':  
                if szoveg[j] < szoveg[j + 1]:
                    szoveg[j], szoveg[j + 1] = szoveg[j + 1], szoveg[j]

    print(f"Buborékrendezés szöveggel: {szoveg}")
   
   
# beszúrásos rendezés
if szam:
    irany = input("A beszúrásos rendezés növekvő vagy csökkenő sorrendben történjen? ")

    for i in range(1, len(szam)):
        kulcs = szam[i]
        j = i - 1
        if irany == 'növekvő':
            while j >= 0 and szam[j] > kulcs:  
                szam[j + 1] = szam[j]
                j -= 1
        elif irany == 'csökkenő':
            while j >= 0 and szam[j] < kulcs:  
                szam[j + 1] = szam[j]
                j -= 1
        szam[j + 1] = kulcs  

    print(f"Beszúrásos rendezés számokkal: {szam}")


if szoveg:
    irany = input("A beszúrásos rendezés növekvő vagy csökkenő sorrendben történjen? ")

    for i in range(1, len(szoveg)):
        kulcs = szoveg[i]
        j = i - 1
        if irany == 'növekvő':
            while j >= 0 and szoveg[j] > kulcs:  
                szoveg[j + 1] = szoveg[j]
                j -= 1
        elif irany == 'csökkenő':
            while j >= 0 and szoveg[j] < kulcs:  
                szoveg[j + 1] = szoveg[j]
                j -= 1
        szoveg[j + 1] = kulcs  

    print(f"Beszúrásos rendezés szövegekkel: {szoveg}")
   
   
#új elem beszúrása
   
uj_elem = input("Adj meg egy új elemet: ")
irany = input("Az új elem beszúrásának iránya növekvő vagy csökkenő legyen? ")

if uj_elem.isdigit():  
    uj_elem = int(uj_elem)
    if irany == 'növekvő':
        for i in range(len(szam)):
            if szam[i] > uj_elem:
                szam.insert(i, uj_elem)
                break
        else:
            szam.append(uj_elem)  
    elif irany == 'csökkenő':
        for i in range(len(szam)):
            if szam[i] < uj_elem:
                szam.insert(i, uj_elem)
                break
        else:
            szam.append(uj_elem)  

    print(f"Frissített szám lista: {szam}")

elif uj_elem.isalpha():  
    if irany == 'növekvő':
        for i in range(len(szoveg)):
            if szoveg[i] > uj_elem:
                szoveg.insert(i, uj_elem)
                break
        else:
            szoveg.append(uj_elem)  
    elif irany == 'csökkenő':
        for i in range(len(szoveg)):
            if szoveg[i] < uj_elem:
                szoveg.insert(i, uj_elem)
                break
        else:
            szoveg.append(uj_elem)  

    print(f"Frissített szöveg lista: {szoveg}")