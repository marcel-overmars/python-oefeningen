# ==========================================================
# UITLEG PROJECT - CAMPING DE VELUWEPOORT
# ==========================================================
#
# In dit project oefen ik met het verwerken van gegevens die
# tijdens het uitvoeren van het programma door de gebruiker
# worden ingevoerd.
#
# Met input() worden verschillende gegevens opgevraagd.
# Numerieke invoer wordt met int() omgezet naar gehele
# getallen, zodat ermee gerekend en vergeleken kan worden.
#
# De ingevoerde gegevens worden vervolgens gebruikt voor
# controles, berekeningen en het samenstellen van een
# reservering. Ook wordt gecontroleerd of een gekozen
# activiteit beschikbaar is.
#
# Gebruikte onderdelen:
# - input()
# - int()
# - variabelen en constanten
# - if, elif en else
# - in
# - lower() en title()
# - lijsten
# - dictionaries
# - items()
# - len()
# - berekeningen met ingevoerde gegevens
# - f-strings
#
# Zelf geprogrammeerd als oefening tijdens het leren van
# Python. ChatGPT hielp met de projectopdracht en feedback.
# ==========================================================

# =====================
# Gast aanmelden
# =====================

naam = input("Wat is je naam? ")
leeftijd = int(input("Hoe oud ben je? "))
woonplaats = input("Wat is je woonplaats? ")
aantal_nachten = int(input("Hoeveel nachten blijft u? "))
print()

# ===================
# Welkomstbericht
# ===================

print(f"Welkom {naam.title()} uit {woonplaats.title()}!")
print()

# =======================
# Leeftijd controleren
# =======================

if leeftijd < 18:
    print(f"{naam.title()} mag alleen onder begeleiding naar binnen!")
elif leeftijd < 65:
    print(f"{naam.title()} heeft normale toegang!")
else:
    print(f"{naam.title()} krijgt het seniorentarief!")
print()

# ================
# Verblijfkosten
# ================

KAMPEERPLAATS = 27
totale_kosten = aantal_nachten * KAMPEERPLAATS

print(f"De totale kosten zijn: €{totale_kosten}")
print()

# ================
# Activiteiten
# ================

activiteiten =[
    'zwembad',
    'fietsverhuur',
    'wandeling',
    'visvijver',
    'restaurant'
]

activiteit = input("Welke activiteit zou je graag willen doen? ")
print()

if activiteit.lower() in activiteiten:
    print(f"De volgende activiteit is nog beschikbaar: {activiteit}")
else:
    print(f"De volgende activiteit is deze week niet beschikbaar: {activiteit}")
print()

# ====================
# Campinggegevens
# ====================

camping = {
    'campingnaam': 'de veluwepoort',
    'plaatsen beschikbaar': 37,
    'medewerkers aanwezig': 6,
    'restaurant open': 'ja'
}

for gegevens, waarde in camping.items():
    print(f"{gegevens.title()}: {waarde}")
print()

# ==============
# Reservering
# ==============

gasten = {
    'naam': naam.title(),
    'leeftijd': leeftijd,
    'woonplaats': woonplaats,
    'aantal nachten': aantal_nachten,
    'gekozen activiteit': activiteit.title(),
    'totale verblijfskosten': totale_kosten
}

for gast, verblijf in gasten.items():
    print(f"{gast}: {verblijf}")
print()

# ========================
# Eindrapport receptie
# ========================

print("==================================")
print("=== DE VELUWEPOORT EINDRAPPORT ===")
print("==================================")
print()
print(f"Naam van de camping: {camping['campingnaam'].title()}")
print(f"Naam van de gast: {naam.title()}")
print(f"Leeftijd van de gast: {leeftijd}")
print(f"Aantal nachten: {aantal_nachten}")
print(f"Totale verblijfskosten: {totale_kosten}")
print(f"Gekozen activiteit: {activiteit}")
print(f"Hoeveel verschillende soorten activiteiten de camping aanbiedt: {len(activiteiten)}")
print(f"Hoeveel plaatsen er beschikbaar zijn: {camping['plaatsen beschikbaar']}")