# ==========================================================
# UITLEG PROJECT - BLACKSMITH ORDER SYSTEM
# ==========================================================
#
# In dit project beheer ik de smederij Iron Hammer.
# Het programma toont wapens, berekent bestellingen en
# verzendkosten, controleert voorraden en registreert klanten.
#
# Gebruikte onderdelen:
# - functies maken en aanroepen met def
# - parameters en argumenten
# - positional en keyword arguments
# - default values
# - return om berekende waarden terug te geven
# - resultaten van functies opnieuw gebruiken
# - dictionaries in een lijst
# - dictionarywaarden opvragen met .get()
# - dictionarywaarden toevoegen en aanpassen
# - for-loops en while-loops
# - if / else en tellers met +=
#
# Het belangrijkste nieuwe onderdeel was return.
# Hiermee kan een functie een waarde teruggeven die
# vervolgens buiten de functie opgeslagen en opnieuw
# gebruikt kan worden, bijvoorbeeld in een berekening
# van verzendkosten.
#
# Daarnaast heb ik oudere Python-onderdelen herhaald,
# waaronder dictionaries, lijsten en while-loops.
#
# Zelf geprogrammeerd als oefening tijdens het leren van
# Python. ChatGPT hielp met de projectopdracht en feedback.
# ==========================================================

# ===========================
# Gegevens van de smederij
# ===========================

smederij = {
    'naam': 'Iron Hammer',
    'plaats': 'Stormwind',
    'status': 'open',
    'bestellingen': 0
}

for smid, gegevens in smederij.items():
    print(f"{smid.title()}: {gegevens}")
print()

# ===============
# Wapens
# ===============

wapen_1 = {
    'naam': 'Iron Sword',
    'prijs': 80,
    'schade': 35,
    'voorraad': 4
}

wapen_2 = {
    'naam': 'Battle Axe',
    'prijs': 120,
    'schade': 55,
    'voorraad': 2
}

wapen_3 = {
    'naam': 'War Hammer',
    'prijs': 150,
    'schade': 70,
    'voorraad': 3
}

wapens =[
    wapen_1,
    wapen_2,
    wapen_3
]

for wapen in wapens:
    print(wapen)
print()

# ==================
# Wapeninformatie
# ==================

def wapen_info(naam, schade, voorraad):
    print(f"Naam: {naam}")
    print(f"Schade: {schade}")
    print(f"Voorraad: {voorraad}")

wapen_info(wapen_1['naam'], wapen_1['schade'], wapen_1['voorraad'])
print()

wapen_info(schade=wapen_1['schade'], naam=wapen_1['naam'], voorraad=wapen_1['voorraad'])
print()

# ==========================
# Bestellingen berekenen
# ==========================

def berekening(prijs, aantal):
    totaal_prijs = prijs * aantal
    return totaal_prijs

bedrag = berekening(80, 3)

print(bedrag)
print()

# ====================
# verzendkosten
# ====================

def extra_kosten(bedrag, verzendkosten=10):
    totaal = bedrag + verzendkosten
    return totaal

totaal_bedrag = extra_kosten(bedrag)

print(totaal_bedrag)
print()

totaal_prijs = extra_kosten(bedrag, 25)

print(totaal_prijs)
print()

# ===========================
# .get() herhaling oefenen
# ===========================

wapen_schade = wapen_3.get('schade')
print(f"Schade van {wapen_3['naam']}: {wapen_schade}")
print()

wapen_gewicht = wapen_3.get('gewicht', f'Gewicht van {wapen_3['naam']} onbekend.')
print(wapen_gewicht)
print()

# ==================================================
# Voorraad controleren en dictionaries aanpassen
# ==================================================

for wapen in wapens:
    if wapen['voorraad'] < 3:
        wapen['status'] = 'bijna uitverkocht'
    else:
        wapen['status'] = 'op voorraad'
    print(wapen)
print()

# =======================
# Klanten registreren
# =======================

klant = ""
klanten_teller = 0

while klant != 'stop':
    klant = input(f"\nTyp 'klant' voor volgende klant of typ 'stop' om te stoppen: ")

    if klant == 'stop':
        print("Klantenregistratie is gesloten!")
    else:
        klanten_teller += 1
        print(f"Klant {klanten_teller} is geholpen.")
print()

smederij['bestellingen'] += klanten_teller

for smid, gegevens in smederij.items():
    print(f"{smid.title()}: {gegevens}")
print()

# ===============
# Eindrapport
# ===============

print("===========================")
print("=== IRON HAMMER RAPPORT ===")
print("===========================")
print()
print(f"Plaats: {smederij['plaats']}")
print(f"Status: {smederij['status']}")
print(f"Bestellingen: {smederij['bestellingen']}")
print()
print("WAPENVOORRAAD")
print()

for wapen in wapens:
    print(wapen)