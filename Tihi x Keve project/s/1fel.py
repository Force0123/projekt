import random
import string

def genRanSzam(szam, also, felso):
                                                #Véletlen számok generálása.#
    return [random.randint(also, felso) for _ in range(szam)]

def genRanSzov(szam):
                                                #Véletlen szöveg az ABC betűiből.#
    chars = string.ascii_letters
    return [''.join(random.choice(chars) for _ in range(random.randint(1, 20))) for _ in range(szam)]

def writeToFile(adat):
                                                 #Kiirja a ki.txt fájlba.#
    with open('ki.txt', 'w') as fajl:
        fajl.write(';'.join(map(str, adat)))

def readFromFile():
                                                 #Beolvassa a ki.txt fájl tartalmát.#
    with open('ki.txt', 'r') as fajl:
        tartalom = fajl.read().strip()
    return tartalom.split(';')

def megfSzam(adat, also, felso):
                                                 #Leellenőrzi hogy megfelelnek e a számok adatai.#
    try:
        szamok = [int(a) for a in adat]
        return all(also <= szam <= felso for szam in szamok)
    except ValueError:
        return False

def megfSzov(adat):
                                                #Leellenőrzi hogy megfelelnek e a betűk adatai.#
    chars = set(string.ascii_letters)
    try:
        strings = [str(a) for a in adat]
        for b in strings:
            if not (1 <= len(b) <= 20):
                return False
            if not all(c in chars for c in b):
                return False
        return True
    except ValueError:
        return False

def main():
    while True:
        print("Válassz egy lehetőséget:")
        print("1. Véletlen számok generálása")
        print("2. Véletlen szövegek generálása")
        print("3. Számok ellenőrzése")
        print("4. Szövegek ellenőrzése")
       
        
        opcio = input("Választás: ")
        
        if opcio == '1':
            szam = int(input("Darabszám: "))
            also = int(input("Alsó határ: "))
            felso = int(input("Felső határ: "))
            szamok = genRanSzam(szam, also, felso)
            writeToFile(szamok)
            print(f"Kapott számok: {szamok}")
        
        elif opcio == '2':
            szam = int(input("Darabszám: "))
            strings = genRanSzov(szam)
            writeToFile(strings)
            print(f"Generált szövegek: {strings}")
        
        elif opcio == '3':
            szam = int(input("Darabszám: "))
            also = int(input("Alsó határ: "))
            felso = int(input("Felső határ: "))
            adat = readFromFile()
            if len(adat) != szam:
                print("Hibás darabszám.")
            elif megfSzam(adat, also, felso):
                print("A számok megfelelnek a feltételeknek.")
            else:
                print("A számok nem felelnek meg a feltételeknek.")
        
        elif opcio == '4':
            szam = int(input("Darabszám: "))
            adat = readFromFile()
            if len(adat) != szam:
                print("Hibás darabszám.")
            elif megfSzov(adat):
                print("A szövegek megfelelnek a feltételeknek.")
            else:
                print("A szövegek nem felelnek meg a feltételeknek.")
        
        
        
        else:
            print("Érvénytelen választás, próbáld újra.")

if __name__ == "__main__":
    main()