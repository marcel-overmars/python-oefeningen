# ==========================================================
# UITLEG PROJECT - EXPEDITIE AVONTURIERSPROFIEL
# ==========================================================
#
# In dit project oefen ik voor het eerst met dictionaries.
# In een dictionary worden gegevens opgeslagen als
# key-value paren. Hierdoor kunnen meerdere gegevens over
# dezelfde avonturier overzichtelijk bij elkaar staan.
#
# Het programma haalt verschillende waarden uit de
# dictionary en gebruikt deze vervolgens voor controles
# en berekeningen, zoals gezondheid, ervaringspunten
# en de hoeveelheid goud.
#
# Daarnaast vergelijk ik met een for-loop twee lijsten om
# te controleren welke gewenste spullen beschikbaar zijn.
#
# Gebruikte onderdelen:
# - dictionaries en key-value paren
# - waarden uit een dictionary ophalen
# - variabelen
# - lists en for-loops
# - if, elif en else
# - in
# - berekeningen
# - f-strings en title()
#
# Zelf geprogrammeerd als oefening tijdens het leren van
# Python. ChatGPT hielp met de projectopdracht en feedback.
# ==========================================================

# ========================
# Avonturiersprofiel
# ========================

avonturier ={
    'naam': 'marcel',
    'leeftijd': 41,
    'beroep': 'jager',
    'level': 17,
    'levenspunten': 85,
    'goudstukken': 800,
    'ervaringspunten': 550,
}

print("==========================")
print("=== AVONTURIERSPROFIEL ===")
print("==========================")
print()
print(f"Naam:\t\t\t{avonturier['naam'].title()}")
print(f"Leeftijd:\t\t{avonturier['leeftijd']}")
print(f"Beroep:\t\t\t{avonturier['beroep'].title()}")
print(f"level:\t\t\t{avonturier['level']}")
print(f"Levenspunten:\t\t{avonturier['levenspunten']}")
print(f"Goudstukken:\t\t{avonturier['goudstukken']}")
print(f"Ervaringspunten:\t{avonturier['ervaringspunten']}")
print()

# ==========================
# Waarden uit het profiel
# ==========================

naam = avonturier['naam']
level = avonturier['level']
levenspunten = avonturier['levenspunten']
goudstukken = avonturier['goudstukken']
ervaringspunten = avonturier['ervaringspunten']

# =======================
# Gezondheidscontrole
# =======================

if levenspunten < 25:
    print(f"De gezondheid van {naam.title()} is kritiek")
elif levenspunten < 50:
    print(f"{naam.title()} is gewond")
elif levenspunten < 80:
    print(f"{naam.title()} is redelijk gezond")
elif levenspunten >= 80:
    print(f"{naam.title()} is in uitstekende conditie")
print()

if level < 5:
    verdiende_punten = 20
elif level < 10:
    verdiende_punten = 40
elif level < 20:
    verdiende_punten = 75
elif level >= 20:
    verdiende_punten = 100

nieuwe_ervaringspunten = ervaringspunten + verdiende_punten

print(f"{naam.title()} had {ervaringspunten} ervaringspunten")
print(f"{naam.title()} verdiende {verdiende_punten} ervaringspunten")
print(f"Nieuwe totaalscore: {nieuwe_ervaringspunten}")
print()

# ===================
# Winkelcontrole
# ===================

expeditiewinkel =[
    'touw',
    'fakkel',
    'zwaard',
    'kaart',
    'voedsel',
    'kompas',
]

gewilde_spullen =[
    'zwaard',
    'health potion',
    'voedsel',
]

for item in gewilde_spullen:
    if item in expeditiewinkel:
        print(f"Het volgende item is nog beschikbaar: {item}")
    else:
        print(f"Het volgende item is uitverkocht: {item}")
print()

# ================
# goudcontrole
# ================

if goudstukken < 25:
    print(f"{naam.title()} heeft bijna geen goud")
elif goudstukken < 75:
    print(f"{naam.title()} heeft een kleine voorraad")
elif goudstukken < 150:
    print(f"{naam.title()} heeft voldoende goud")
elif goudstukken >= 150:
    print(f"{naam.title()} is een rijke avonturier")
print()

# =================
# Eindrapport
# =================

print("=============================")
print("=== EXPEDITIE EINDRAPPORT ===")
print("=============================")
print()
print(f"Naam: {naam}")
print(f"Beroep: {avonturier['beroep']}")
print(f"Level: {level}")
print(f"Levenspunten: {levenspunten}")
print(f"Goudstukken: {goudstukken}")
print(f"Oude ervaringspunten: {ervaringspunten}")
print(f"Verdiende ervaringspunten: {verdiende_punten}")
print(f"Nieuwe totaalscore: {nieuwe_ervaringspunten}")