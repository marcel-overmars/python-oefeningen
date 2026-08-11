# ==========================================================
# UITLEG PROJECT - HERBERGREGISTRATIE
# ==========================================================
#
# In dit project oefen ik verder met dictionaries. Ik begin
# met een lege dictionary en voeg daarna stap voor stap
# verschillende key-value paren toe met gegevens over een
# reiziger.
#
# Een aantal waarden uit de dictionary wordt opgeslagen in
# aparte variabelen. Later worden nieuwe gegevens aan de
# bestaande dictionary toegevoegd, zoals het kamernummer
# en het aantal nachten.
#
# Met een if-elif-statement wordt gecontroleerd hoeveel
# goudstukken de reiziger heeft en welke kamer hij daarmee
# kan betalen.
#
# Gebruikte onderdelen:
# - een lege dictionary maken
# - nieuwe key-value paren toevoegen
# - waarden uit een dictionary ophalen
# - dictionarywaarden opslaan in variabelen
# - if en elif
# - f-strings en title()
#
# Zelf geprogrammeerd als oefening tijdens het leren van
# Python. ChatGPT hielp met de projectopdracht en feedback.
# ==========================================================

# =======================
# dictionary gegevens
# =======================

reiziger = {}

reiziger['naam'] = 'marcel'
reiziger['leeftijd'] = 41
reiziger['beroep'] = 'jager'
reiziger['goudstukken'] = 250

print(reiziger)
print()

# ==========================
# Variabelen van gegevens
# ==========================

naam = reiziger['naam']
beroep = reiziger['beroep']
goudstukken = reiziger['goudstukken']

# ===============================
# toevoegingen aan dictionary
# ===============================

reiziger['kamer'] = 12
reiziger['nachten'] = 5

print(f"{naam.title()} krijgt kamer {reiziger['kamer']} voor {reiziger['nachten']} nachten!")
print()

# =======================
# goudstukken controle
# =======================

if goudstukken < 50:
    print(f"{naam.title()} heeft weinig goud!")
elif goudstukken < 150:
    print(f"{naam.title()} heeft voldoende goud!")
elif goudstukken >= 150:
    print(f"{naam.title()} kan een luxe kamer betalen!")
print()