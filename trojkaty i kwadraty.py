import math
while True:

    zmiennik =input("jaką figurę wybierasz płaska-(True), przestrzenna-(False) lub zakończ program (exit): ").strip().lower()
    
    if zmiennik == 'exit':
        print("Koniec programu.")
        break
    zmiennik = zmiennik =='true'

    if zmiennik:
        zmiennik_plaska = input("jaka figure plaska wybierasz, kwadrat - 1, prostokat - 2, rownoleglobok -3, trapez - 4, trojkat - 5, trojkat rownoboczny - 6, kolo - 7, romb - 8:  ")

        if zmiennik_plaska == '1':
            a = float(input("podaj długosc boku kwadratu"))
            kwadrat = a*a
            print("pole wynosi: ",kwadrat)

        elif zmiennik_plaska == '2':
            a = float(input("podaj dlugosc pierwszego boku: "))
            b = float(input("podaj dlugosc drugiego boku: "))
            prostokat = a*b
            print("pole wynosi: ",prostokat)

        elif zmiennik_plaska == '3':
            a = float(input("podaj dlugosc boku: "))
            h = float(input("podaj wysokosc tej figury: "))
            rownoleglobok = a*h
            print("pole wynosi: ",rownoleglobok)

        elif zmiennik_plaska == '4':
            a = float(input("podaj dlugosc boku: "))
            b = float(input("podaj dlugosc drugiego boku: "))
            h = float(input("podaj wysokosc tej figury: "))
            trapez = ((a+b)*h)/2
            print("pole wynosi: ",trapez)

        elif zmiennik_plaska == '5':
            a = float(input("podaj dlugosc boku: "))
            h = float(input("podaj wysokosc tej figury: "))
            trojkat = (a*h)*0,5
            print("pole wynosi: ",trojkat)

        elif zmiennik_plaska == '6':
            a = float(input("podaj dlugosc boku: "))
            trojkat_r = (a**2 * math.sqrt(3))/4
            print("pole wynosi: ",trojkat_r)

        elif zmiennik_plaska == '7':
            PI = math.pi
            r = float(input("podaj promien od srodka kola: "))
            kolo = (PI*r**2)
            print("pole kola wynosi: ",kolo)

        elif zmiennik_plaska == '5':
            e = float(input("podaj dlugosc przekontnej e: "))
            f = float(input("podaj dlugosc przekontnej f: "))
            romb = (e*f)/2
            print("pole wynosi: ",romb) 
    else:
        zmiennik_przestrzen = input("jaka figure przestrzenna wybierasz, szescian - 1, prostopadloscian - 2, graniastoslup - 3, ostroslup - 4, walec - 5, stozek - 6, kula - 6:  ")

        if zmiennik_przestrzen == '1':
            a = float(input("podaj dlugosc boku: "))
            szescian = (6*a**2)
            print("pole powierzchni tej figury to: ",szescian)

        elif zmiennik_przestrzen == '2':
            a = float(input("podaj dlugosc 1 boku: "))
            b = float(input("podaj dlugosc 2 boku: "))
            c = float(input("podaj dlugosc 3 boku: "))
            prostopad = (2*a*b + 2*a*c + 2*b*c)
            print("pole powierzchni tej figury to: ",prostopad)

        elif zmiennik_przestrzen == '3':
            Pp = float(input("podaj pole powierzchni podstawy: "))
            Pb = float(input("podaj pole powierzchni boku: "))
            graniastoslup = 2*Pp+Pb
            print("pole powierzchni tej figury to: ",graniastoslup)

        elif zmiennik_przestrzen == '3':
            Pp = float(input("podaj pole powierzchni podstawy: "))
            Pb = float(input("podaj pole powierzchni boku: "))
            ostroslup = Pp+Pb
            print("pole powierzchni tej figury to: ",ostroslup)
            
        elif zmiennik_przestrzen == '4':
            PI = math.pi
            r = float(input("podaj dlugosc promienia: "))
            h = float(input("podaj wysokosc: "))
            walec = 2*(PI*r**2)+2*(PI*r*h)
            print("pole powierzchni tej figury to: ",walec)

        elif zmiennik_przestrzen == '4':
            PI = math.pi
            r = float(input("podaj dlugosc promienia: "))
            l = float(input("podaj L: "))
            stozek = (PI*r**2)+(PI*r*l)
            print("pole powierzchni tej figury to: ",stozek)

        elif zmiennik_przestrzen == '4':
            PI = math.pi
            r = float(input("podaj dlugosc promienia: "))
            kula = 4*(PI*r**2)
            print("pole powierzchni tej figury to: ",kula)

    print()