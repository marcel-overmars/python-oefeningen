# ==========================================================
# UITLEG PROJECT - RUIMTEMISSIE BEMANNINGSREGISTRATIE
# ==========================================================
#
# In dit project oefen ik verder met dictionaries. Ik begin
# met een lege dictionary en voeg stap voor stap gegevens
# van een bemanningslid toe.
#
# De waarden uit de dictionary worden gebruikt voor
# controles op ervaring en gezondheid. Later worden nieuwe
# key-value paren toegevoegd met de toegewezen missie.
#
# Daarnaast oefen ik eerdere stof door uitrustingslijsten
# te vergelijken, meerdere technische problemen te
# controleren en brandstofmetingen te verwerken.
#
# Gebruikte onderdelen:
# - dictionaries en key-value paren
# - dictionarywaarden toevoegen en ophalen
# - variabelen
# - lists en for-loops
# - if, elif en else
# - meerdere losse if-statements
# - in
# - range() en append()
# - slices, min(), max(), sum() en len()
# - gemiddelde berekenen
# - f-strings, title() en upper()
#
# Zelf geprogrammeerd als oefening tijdens het leren van
# Python. ChatGPT hielp met de projectopdracht en feedback.
# ==========================================================

# =================
# Bestemmingen
# =================

bestemmingen =(
    'mars',
    'europa',
    'titan',
    'ganymedes',
    'enceladus',
)

# ===================================
# Registratie nieuw bemanningslid
# ===================================

bemanningslid = {}

bemanningslid['naam'] = 'dennis'
bemanningslid['leeftijd'] = 28
bemanningslid['functie'] = 'kapitein'
bemanningslid['ervaringsscore'] = 85
bemanningslid['gezondheidsscore'] = 45
bemanningslid['credits'] = 125

print(bemanningslid)
print()

# =============================
# Variabelen van de gegevens
# =============================

naam = bemanningslid['naam']
functie = bemanningslid['functie']
ervaringsscore = bemanningslid['ervaringsscore']
gezondheidsscore = bemanningslid['gezondheidsscore']
credits = bemanningslid['credits']

# =========================
# geschiktheidscontrole
# =========================

if ervaringsscore < 25:
    print(f"{naam.title()} is een leerling!")
elif ervaringsscore < 50:
    print(f"{naam.title()} is een junior bemanningslid!")
elif ervaringsscore < 75:
    print(f"{naam.title()} is een ervaren bemanningslid!")
elif ervaringsscore >= 75:
    print(f"{naam.title()} is een elitebemanningslid!")

# ======================
# Gezondheidscontrole
# ======================

if gezondheidsscore < 30:
    print(f"{naam.title()} is niet geschikt voor vertrek!")
elif gezondheidsscore < 60:
    print(f"{naam.title()} heeft extra medische controle nodig!")
elif gezondheidsscore < 80:
    print(f"{naam.title()} is goedgekeurd!")
elif gezondheidsscore >= 80:
    print(f"{naam.title()} is in uitstekende conditie!")
print()

# ===========================
# Verkregen missiegegevens
# ===========================

bemanningslid['bestemming'] = 'mars'
bemanningslid['missieduur'] = '3 maanden'
bemanningslid['ruimtepaknummer'] = 7

print(f"{naam.title()} is toegewezen aan de missie naar {bemanningslid['bestemming']}!")
print(f"De missie duurt {bemanningslid['missieduur']}!")
print(f"Ruimtepaknummer: {bemanningslid['ruimtepaknummer']}")
print()

# =======================
# Uitrustingcontrole
# =======================

uitrusting =[
    'zuurstoftank',
    'ruimtepak',
    'helm',
    'voedselpakket',
    'gereedschapskist',
    'communicatieset',
    'noodpakket',
]

uitrusting_aanvraag =[
    'ruimtepak',
    'helm',
    'brandstofcel',
    'communicatieset',
    'water',
    'noodpakket',
]

for aanvraag in uitrusting_aanvraag:
    if aanvraag in uitrusting:
        print(f"De volgende uitrusting is beschikbaar: {aanvraag.title()}")
    else:
        print(f"De volgende uitrusting is niet beschikbaar: {aanvraag.upper()}")
print()

# ==========================
# technische problemen
# ==========================

problemen =[
    'defecte luchtsluis',
    'brandstoflek',
    'communicatiestoring',
    'beschadigd zonnepaneel',
]

for probleem in problemen:
    if probleem == 'defecte luchtsluis':
        print("Luchtsluis in sectie b is defect, actie is noodzakelijk!")
    if probleem == 'brandstoflek':
        print("Brandstoflek dient gerepareerd te worden!")
    if probleem == 'communicatiestoring':
        print("Vervang de communicatieset door een set dat wel werkt!")
    if probleem == 'beschadigd zonnepaneel':
        print("Test het zonnepaneel en als het probleem niet gevonden wordt, vervangen!")
print()

# ===============================
# Dagelijkse brandstofmetingen
# ===============================

brandstofmetingen = []

for uur in range(1, 9):
    brandstof = uur * 15
    brandstofmetingen.append(brandstof)

gemiddelde = sum(brandstofmetingen) / len(brandstofmetingen)

print(f"Alle metingen: {brandstofmetingen}")
print(f"Eerste 3 metingen: {brandstofmetingen[:3]}")
print(f"Laatste 3 metingen: {brandstofmetingen[-3:]}")
print(f"Laagste meting: {min(brandstofmetingen)}")
print(f"Hoogste meting: {max(brandstofmetingen)}")
print(f"Het totaal van de metingen: {sum(brandstofmetingen)}")
print(f"Gemiddelde van de metingen: {gemiddelde}")
print(f"Aantal metingen: {len(brandstofmetingen)}")
print()

# ================
# Eindrapport
# ================

print("================================")
print("=== RUIMTEMISSIE EINDRAPPORT ===")
print("================================")
print()
print(f"Naam: {naam.title()}")
print(f"Functie: {functie.title()}")
print(f"Bestemming: {bemanningslid['bestemming'].title()}")
print(f"Missieduur: {bemanningslid['missieduur']}")
print(f"Ervaringsscore: {ervaringsscore}")
print(f"Gezondheidsscore: {gezondheidsscore}")
print(f"Credits: {credits}")
print(f"Ruimtepaknummer: {bemanningslid['ruimtepaknummer']}")
print(f"Aantal beschikbare uitrustingsstukken: {len(uitrusting)}")
print(f"Aantal brandstofmetingen: {len(brandstofmetingen)}")
print(f"Laagste brandstofmeting: {min(brandstofmetingen)}")
print(f"Hoogste brandstofmeting: {max(brandstofmetingen)}")
print(f"Gemiddelde brandstofmeting: {gemiddelde}")