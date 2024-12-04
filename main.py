import random
import time

# Statystyki postaci
o_sila = 10
p_sila = 7
a_sila = 4
cz_sila = 6
#szybkosc
o_szyb = 4
p_szyb = 6
a_szyb = 10
cz_szyb = 15
#hp
o_hp = 15
p_hp = 12
a_hp = 9
cz_hp = 7

# Statystyki korposa
k_hp = 7
max_k_hp = 7
k_dmg = 5
k_szyb = 4

# Statystyki lamusa
l_hp = 10
l_max_hp = 10
l_dmg = 4
l_szyb = 6
# Słownik bohaterów
bohaterowie = {
    1: {"nazwa": "orc", "hp": o_hp, "szyb": o_szyb, "sila": o_sila},
    2: {"nazwa": "paladyn", "hp": p_hp, "szyb": p_szyb, "sila": p_sila},
    3: {"nazwa": "anime", "hp": a_hp, "szyb": a_szyb, "sila": a_sila},
    4: {"nazwa": "czarodziej", "hp": cz_hp, "szyb": cz_szyb, "sila": cz_sila}
}

# Wybór bohatera
bohater = 0
while True:
    wybor_p = input("Wybierz postać: 1. Orc: (DOPAKOWANY SEBIKS, NIELICZY SIE JAK, LICZOM SIE EFEKTY) 2. Paladyn: (ZUL PO DWOCH BROWARACH I SETCE, KUPIONE U PANI BASI W SKLEPIE OBOK) 3. Anime: (DZIEWCZYNKA CO UBIERA SIE W POSTACIE Z ULUBIONYCH ANIME) 4. Czarodziej:(STARY ZGRED Z DEMENCJĄ, UCIEKINIER WARSZAWASKIEGO ZAKLADU PSYCHIATRYCZNEGO DREWNICA) ")
    if wybor_p in ("1", "2", "3", "4"):
        bohater = int(wybor_p)
        wybrany_bohater = bohaterowie[bohater]
        print(f"Wybrano {wybrany_bohater['nazwa']}: Siła: {wybrany_bohater['sila']}, Szybkość: {wybrany_bohater['szyb']}, HP: {wybrany_bohater['hp']}")
        break
    else:
        print("Wybierz jeszcze raz :)")
time.sleep (4)
print("")
# Historia i rozgrywka
print(f"Teraz czas wprowadzić Cię w historię.... Dawno,dawno,dawno temu, a wzasadzie to nie bo tydzien temu ", wybrany_bohater['nazwa'])
print("wybrał sie do roboty... idąc po miescie niestety tak sie zlozylo, ze jego zycie to teraz gra i ty decydujesz co sie stanie.")
time.sleep (2)
print("")
print("Możesz wybierać różne ścieżki ,każdy wybór będzie miał jakikś wpływ na historię, ale gra jest wciąż w fazie beta więc ciesz tym co masz :).")
time.sleep (1)
print("Gra nie jest skomplikowana, czasami jest szansa na spotkanie przeciwnika z którym możesz walczyć")
time.sleep (1)
print("system walki też jest prosty, jeśli twoja szybkośc jest większa niż przeciwnika to zadajesz pierwszy cios, jeśli jest równa lub mniejsza to on uderza pierwszy")
print("")
print("")

time.sleep (4)
sciezka = input(" 1 - prawo, 2 - lewo: ")
if sciezka == ("1"):
    print("Idąc w prawo trafiasz do alejki z straganami obiadowymi i dziwnymi ludźmi. Przypominają oni szczury... To korposy. Jesteś nieuważny i idąc wpadasz na jednego")
    time.sleep(2)
    print("WALCZ !")
    time.sleep (2)
    # Walka z korposem
    bohater_atakuje_pierwszy = wybrany_bohater['szyb'] > k_szyb

    while k_hp > 0 and wybrany_bohater['hp'] > 0:
        if bohater_atakuje_pierwszy:
            #bohater
            print(f"{wybrany_bohater['nazwa']} zadaje cios!")
            k_hp -= wybrany_bohater['sila']
            time.sleep(2)
            print(f"Korpos ma teraz {k_hp} HP.")

            if k_hp <= 0:
                print("Pokonałeś korposa! Możesz iść dalej.")
                k_hp = max_k_hp  # Reset HP korposa
                break 
            #korpos 
            print("Korpos atakuje!")
            time.sleep(2)
            wybrany_bohater['hp'] -= k_dmg
            print(f"Twój bohater ma teraz {wybrany_bohater['hp']} HP.")
            time.sleep(2)
            
            if wybrany_bohater['hp'] <= 0:
                print("Zostałeś pokonany. Koniec gry.")
                exit()
        else:
            # Korpos
            print("Korpos atakuje!")
            time.sleep(2)
            wybrany_bohater['hp'] -= k_dmg
            print(f"Twój bohater ma teraz {wybrany_bohater['hp']} HP.")
            time.sleep(2)
            
            if wybrany_bohater['hp'] <= 0:
                print("Zostałeś pokonany. Koniec gry.")
                exit()

            # Bohater
            print(f"{wybrany_bohater['nazwa']} atakuje!")
            k_hp -= wybrany_bohater['sila']
            time.sleep(2)
            print(f"Korpos ma teraz {k_hp} HP.")
            
            if k_hp <= 0:
                print("Pokonałeś korposa! Możesz iść dalej.")
                k_hp = max_k_hp  
                break 

elif sciezka == ("2"):
    print("idziesz w lewo i bezpiecznie docierasz do sklepu przed robotą.")
    print("po wyjściu zaczepia cie lamus pospolity. Frajer myśli ,że jest kims jak ci pogrozi i po obraża ale ty nie jesteś frajem i potrafisz  przyj***. Więc tak postanawiasz zrobić")
    time.sleep(2)
    print (" WALCZ !")
    time.sleep(2)
    bohater_atakuje_pierwszy = wybrany_bohater['szyb'] > l_szyb

    while l_hp > 0 and wybrany_bohater['hp'] > 0:
        if bohater_atakuje_pierwszy:
            #bohater
            print(f"{wybrany_bohater['nazwa']} zadaje cios!")
            l_hp -= wybrany_bohater['sila']
            time.sleep(2)
            print(f"Lamus ma teraz {l_hp} HP.")

            if l_hp <= 0:
                print("Pokonałeś lamusa! Możesz iść dalej.")
                l_hp = l_max_hp  # Reset HP lamusa
                break 
            #lamus 
            print("Korpos atakuje!")
            time.sleep(2)
            wybrany_bohater['hp'] -= l_dmg
            print(f"Twój bohater ma teraz {wybrany_bohater['hp']} HP.")
            time.sleep(2)
            
            if wybrany_bohater['hp'] <= 0:
                print("Zostałeś pokonany. Koniec gry.")
                exit()
        else:
            # lamus
            print("Lamus atakuje!")
            time.sleep(2)
            wybrany_bohater['hp'] -= l_dmg
            print(f"Twój bohater ma teraz {wybrany_bohater['hp']} HP.")
            time.sleep(2)
            
            if wybrany_bohater['hp'] <= 0:
                print("Zostałeś pokonany. Koniec gry.")
                exit()

            # Bohater
            print(f"{wybrany_bohater['nazwa']} atakuje!")
            l_hp -= wybrany_bohater['sila']
            time.sleep(2)
            print(f"Lamus ma teraz {l_hp} HP.")
            
            if l_hp <= 0:
                print("Pokonałeś Lamusa! Możesz iść dalej.")
                l_hp = l_max_hp 
                break 
time.sleep(3)
print("")
print(" GRA W FAZIE TWORZENIA ,DZIĘKI ZA GRE :)")
print("pomysły to: 1. regeneracja zdrowia za przedmioty 2.ekwipunek 3.Specjane umiejętności ładowane pzrez pokonywananie przeciwników, 4.więcej przeciwnikó")