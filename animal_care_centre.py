# ==========================================================
# UITLEG PROJECT - HAPPY PAWS
# ==========================================================
#
# In dit project maak ik een eenvoudig registratiesysteem
# voor een dierenopvang. Dieren worden geregistreerd en
# opgeslagen in een lijst. Daarnaast worden leeftijden
# berekend en de administratie bijgewerkt.
#
# Gebruikte onderdelen:
# - Dictionaries en lijsten
# - For-loops
# - Functies met def
# - Optionele parameters en standaardwaarden
# - If/else-controles
# - Return om waarden terug te geven
#
# Het belangrijkste oefenonderdeel was het werken met
# optionele parameters, waaronder een lege string ("").
#
# Dit project heb ik zelfstandig en uit mijn hoofd
# geprogrammeerd. ChatGPT hielp met de opdracht en feedback.
# ==========================================================

# ================================
# Gegevens van de dierenopvang
# ================================

dierenopvang_gegevens = {
    'naam': 'Happy Paws',
    'locatie': 'Apeldoorn',
    'aantal dieren': 0,
    'status': 'geopend'
}

for dierenopvang, gegevens in dierenopvang_gegevens.items():
    print(f"{dierenopvang.title()}: {gegevens}")
print()

# =======================
# Dierenregistratie
# =======================

def registreer_dier(naam, diersoort, bijnaam=""):
    if bijnaam:
        volledige_omschrijving = f"{naam.title()}, {bijnaam.title()}, {diersoort}"
    else:
        volledige_omschrijving = f"{naam.title()}, {diersoort}"
    return volledige_omschrijving

dier_1 = registreer_dier('max', 'hond')
dier_2 = registreer_dier('luna', 'kat', 'luutje')
dier_3 = registreer_dier('rocky', 'hond')
dier_4 = registreer_dier('bella', 'konijn', 'belle')

print(f"Dierenomschrijving: {dier_1}")
print(f"Dierenomschrijving: {dier_2}")
print(f"Dierenomschrijving: {dier_3}")
print(f"Dierenomschrijving: {dier_4}")
print()

# =================
# Dierenlijst
# =================

dieren = []

dieren.append(dier_1)
dieren.append(dier_2)
dieren.append(dier_3)
dieren.append(dier_4)

for dier in dieren:
    print(dier)
print()

# =======================
# Leeftijd berekenen
# =======================

def bereken_leeftijd(huidige_leeftijd, jaren_erbij=2):
    nieuwe_leeftijd = huidige_leeftijd + jaren_erbij
    return nieuwe_leeftijd

leeftijd_max = bereken_leeftijd(4)
leeftijd_luna = bereken_leeftijd(2)

print(f"Leeftijd van Max over 2 jaar: {leeftijd_max} jaar.")
print(f"Leeftijd van Luna over 2 jaar: {leeftijd_luna} jaar.")
print()

# ==========================
# Administratie bijwerken
# ==========================

dierenopvang_gegevens['aantal dieren'] += len(dieren)

for dierenopvang, gegevens in dierenopvang_gegevens.items():
    print(f"{dierenopvang.title()}: {gegevens}")
print()

# ===============
# Eindrapport
# ===============

print("==================")
print("=== HAPPY PAWS ===")
print("==================")
print()
print(f"Locatie: {dierenopvang_gegevens['locatie']}")
print(f"Status: {dierenopvang_gegevens['status']}")
print(f"Aantal dieren: {dierenopvang_gegevens['aantal dieren']}")
print()
print("GEREGISTREERDE DIEREN")
print()

for dier in dieren:
    print(dier)
print()

print("LEEFTIJD OVER 2 JAAR")
print()
print(f"Max: {leeftijd_max} jaar")
print(f"Luna: {leeftijd_luna} jaar")