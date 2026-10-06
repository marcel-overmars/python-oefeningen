# ==========================================================
# UITLEG PROJECT - ORION STATION
# ==========================================================
#
# In dit project beheer ik het ruimtestation Orion Station.
# Het programma registreert ruimteschepen, controleert
# brandstof en status en houdt aangekomen schepen bij.
#
# Gebruikte onderdelen:
# - functies maken en aanroepen
# - parameters en argumenten
# - positional arguments
# - keyword arguments
# - default values
# - dictionaries en lijsten
# - meerdere dictionaries in een lijst
# - dictionarywaarden opvragen met .get()
# - dictionarywaarden aanpassen
# - for-loops
# - while-loop
# - if / elif / else
# - input van de gebruiker
# - tellers met +=
#
# Het belangrijkste nieuwe onderdeel was het werken met
# keyword arguments en default values. Een parameter kan een
# standaardwaarde krijgen die automatisch wordt gebruikt als
# bij het aanroepen geen andere waarde wordt meegegeven.
#
# Daarnaast heb ik oudere stof herhaald door dictionaries in
# een lijst te plaatsen, deze met een for-loop te controleren
# en waarden in de dictionaries aan te passen.
#
# Zelf geprogrammeerd als oefening tijdens het leren van
# Python. ChatGPT hielp met de projectopdracht en feedback.
# ==========================================================

# =====================
# Stationsgegevens
# =====================

stationsgegevens = {
    'naam': 'Orion Station',
    'sector': 'Alpha-7',
    'status': 'operationeel',
    'aangekomen schepen': 0
}

for station, gegevens in stationsgegevens.items():
    print(f"{station.title()}: {gegevens}")
print()

# ============================
# Functie met default value
# ============================

def aankondiging(schip, type_schip='transport'):
    print(f"\n{schip.title()} is aangekomen.")
    print(f"Het type schip: {type_schip}")

aankondiging('voyager')
aankondiging('odyssey', 'onderzoeksschip')
print()

# ==================================
# Positional en keyword arguments
# ==================================

def ruimteschip(naam, kapitein, bemanning):
    print(f"\nNaam: {naam.title()}")
    print(f"Kapitein: {kapitein.title()}")
    print(f"Bemanning: {bemanning}")

ruimteschip('voyager', 'marcel', 8)
ruimteschip(kapitein='dennis', bemanning=12, naam='odyssey')
print()

# ===================
# Schepenregister
# ===================

schip_1 = {
    'naam': 'odyssey',
    'brandstof': 80,
    'status': 'onderweg'
}

schip_2 = {
    'naam': 'voyager',
    'brandstof': 35,
    'status': 'onderweg'
}

schip_3 = {
    'naam': 'endeavour',
    'brandstof': 60,
    'status': 'onderweg'
}

schepen = [
    schip_1,
    schip_2,
    schip_3
]

for schip in schepen:
    print(schip)
print()

# =====================
# Gegevens opvragen
# =====================

brandstof = schip_1.get('brandstof')
print(f"Huidige brandstof van Odyssey: {brandstof}")
print()

schade = schip_1.get('schade', 'Er is geen schade bekend in het systeem.')
print(schade)

# ==========================
# Dictionaries aanpassen
# ==========================

for schip in schepen:
    if schip['brandstof'] < 50:
        schip['status'] = 'bijtanken'
    elif schip['brandstof'] >= 50:
        schip['status'] = 'goedgekeurd'

    print(schip)
print()

# ======================
# Aankomstregistratie
# ======================

aangekomen_schip = ""

schepen_teller = 0

while aangekomen_schip != 'stop':
    aangekomen_schip = input("voer de naam van het schip in of druk op 'stop': ")

    if aangekomen_schip == 'stop':
        print(f"Schepenregistratie gesloten.")
    else:
        schepen_teller += 1
        print(f"Aantal geregistreerde schepen: {schepen_teller}")
print()

stationsgegevens['aangekomen schepen'] += schepen_teller

for station, gegevens in stationsgegevens.items():
    print(f"{station.title()}: {gegevens}")
print()

# ===================
# Statusfunctie
# ===================

def statusfunctie(naam, aantal_schepen, status='operationeel'):
    print(f"Naam: {naam.title()}")
    print(f"Aantal schepen: {aantal_schepen}")
    print(f"Status: {status}")

statusfunctie(stationsgegevens['naam'], stationsgegevens['aangekomen schepen'])
print()

statusfunctie(stationsgegevens['naam'], stationsgegevens['aangekomen schepen'], 'nachtmodus')
print()

# =================
# Eindrapport
# =================

print("=====================")
print("=== ORION STATION ===")
print("=====================")
print()
print(f"Sector: {stationsgegevens['sector']}")
print(f"Status: {stationsgegevens['status']}")
print(f"Aangekomen schepen: {stationsgegevens['aangekomen schepen']}")
print()
print("SCHEPENREGISTER")
print()

for schip in schepen:
    print(schip)