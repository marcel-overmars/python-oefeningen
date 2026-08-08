# ==========================================================
# UITLEG PROJECT - FITNESSCENTRUM LEDENCONTROLE
# ==========================================================
#
# In dit project heb ik verder geoefend met if-statements
# en meerdere elif-blokken. Het belangrijkste nieuwe onderdeel
# was dat een if-elif-keten niet verplicht hoeft te eindigen
# met een else-blok.
#
# Ik begin met een ledenlijst waarin ik gegevens wijzig door:
# - een bestaand item te vervangen;
# - een nieuw lid toe te voegen met append();
# - een lid te verwijderen met pop();
# - het aantal actieve leden te tellen met len().
#
# Daarna maak ik gegevens voor meerdere sporters. Met
# if-elif-ketens bepaal ik op basis van hun trainingsscore
# welk trainingsniveau bij hen hoort:
# - beginner
# - recreatief
# - gevorderd
# - expert
#
# Hierbij gebruik ik voor de laatste mogelijkheid bewust een
# extra elif in plaats van een else-blok.
#
# Vervolgens gebruik ik opnieuw een if-elif-keten om één
# sporter in een leeftijdscategorie te plaatsen. Ook hier
# controleert iedere mogelijkheid een specifieke voorwaarde.
#
# Bij de faciliteiten oefen ik opnieuw met:
# - in
# - not in
# - if
# - else
#
# Hiermee controleer ik of bepaalde faciliteiten wel of niet
# beschikbaar zijn.
#
# Voor de trainingsuren maak ik met een for-loop en range()
# automatisch gegevens voor zeven dagen. Deze waarden sla ik
# op in een lijst met append().
#
# Daarna analyseer ik de trainingsgegevens met:
# - slices
# - min()
# - max()
# - sum()
# - len()
#
# Ook bereken ik het gemiddelde aantal trainingsuren door het
# totale aantal uren te delen door het aantal metingen.
#
# Tot slot maak ik een eindrapport waarin de belangrijkste
# gegevens van het fitnesscentrum worden samengevat.
#
# Met dit project heb ik geoefend met:
# - lists
# - append()
# - pop()
# - indexen aanpassen
# - variabelen
# - if
# - elif
# - else
# - meerdere elif-blokken
# - in
# - not in
# - for-loops
# - range()
# - slices
# - len()
# - min()
# - max()
# - sum()
# - gemiddelde berekenen
# - title()
# - f-strings
#
# Dit project is volledig door mijzelf geprogrammeerd als
# oefening tijdens het leren van Python. ChatGPT heeft alleen
# geholpen met uitleg, feedback en het bedenken van de
# projectopdracht.
# ==========================================================

lijn = "======================================="

# ==============
# Ledenlijst
# ==============

print(lijn)
print()

leden =[
    'marcel',
    'dennis',
    'bianca',
    'sander',
    'iris',
    'alice',
    'peter',
]

leden[0] = 'dylano'
leden.append('jayden')
bevroren = leden.pop(-2)

print("De actuele ledenlijst:")
print(leden)
print()
print(f"Aantal actuele leden: {len(leden)}")
print()
print(f"Van het volgende lid is het lidmaatschap bevroren: {bevroren.title()}")
print()
print(lijn)
print()

# =====================
# Trainingsniveau
# =====================

naam_1 = 'dennis'
leeftijd_1 = 40
trainingsscore_1 = 30

naam_2 = 'bianca'
leeftijd_2 = 43
trainingsscore_2 = 77

naam_3 = 'iris'
leeftijd_3 = 24
trainingsscore_3 = 53

if trainingsscore_1 < 26:
    print(f"{naam_1.title()} is een beginner!")
elif trainingsscore_1 < 51:
    print(f"{naam_1.title()} is recreatief!")
elif trainingsscore_1 < 76:
    print(f"{naam_1.title()} is gevorderd!")
elif trainingsscore_1 <= 100:
    print(f"{naam_1.title()} is expert")
print()

if trainingsscore_2 < 26:
    print(f"{naam_2.title()} is een beginner!")
elif trainingsscore_2 < 51:
    print(f"{naam_2.title()} is recreatief!")
elif trainingsscore_2 <76:
    print(f"{naam_2.title()} is gevorderd!")
elif trainingsscore_2 <= 100:
    print(f"{naam_2.title()} is expert!")
print()

if trainingsscore_3 < 26:
    print(f"{naam_3.title()} is een beginner!")
elif trainingsscore_3 < 51:
    print(f"{naam_3.title()} is recreatief!")
elif trainingsscore_3 < 76:
    print(f"{naam_3.title()} is gevorderd!")
elif trainingsscore_3 <= 100:
    print(f"{naam_3.title()} is expert!")
print()
print(lijn)
print()

# ===================================
# leeftijdscategorie voor 1 sporter
# ===================================

if leeftijd_1 < 18:
    print(f"{naam_1.title()} is een jeugdlid!")
elif leeftijd_1 <30:
    print(f"{naam_1.title()} is jongvolwassene!")
elif leeftijd_1 <50:
    print(f"{naam_1.title()} is een volwassen lid!")
elif leeftijd_1 >= 50:
    print(f"{naam_1.title()} is een seniorlid!")
print()
print(lijn)
print()

beschikbare_faciliteiten =[
    'fitnesszaal',
    'sauna',
    'zwembad',
    'bokszak',
    'roeimachine',
    'loopband',
]

if 'zwembad' in beschikbare_faciliteiten:
    print("Het zwembad is beschikbaar!")
else:
    print("Het zwembad is momenteel niet beschikbaar!")
print()

if 'spinningruimte' not in beschikbare_faciliteiten:
    print("De spinningruimte is momenteel niet beschikbaar!")
else:
    print("De spinningruimte is beschikbaar!")
print()
print(lijn)
print()

# ===========================
# Trainingsuren van de week
# ===========================

trainingsuren = []

for dag in range(1, 8):
    trainingsuur = dag * 0.5
    trainingsuren.append(trainingsuur)

gemiddelde_uren = sum(trainingsuren) / len(trainingsuren)

print(f"Trainingsuur per dag: {trainingsuren}")
print(f"Trainingsuren per dag de eerste 3 dagen: {trainingsuren[:3]}")
print(f"trainingsuren per dag de laatste 3 dagen: {trainingsuren[-3:]}")
print(f"De minste uren op een trainingsdag: {min(trainingsuren)}")
print(f"De meeste uren op een trainingsdag: {max(trainingsuren)}")
print(f"Totaal aantal uren getraind in de week: {sum(trainingsuren)}")
print(f"Het gemiddelde getrainde uren in de week: {gemiddelde_uren}")
print(f"Het aantal gemeten dagen: {len(trainingsuren)}")
print()
print(lijn)
print()

# ===============
# Eindrapport
# ===============

print("=================================")
print("=== EINDRAPPORT LEDENCONTROLE ===")
print("=================================")
print()
print(f"Aantal actieve leden: {len(leden)}")
print(f"Naam van het lid met het bevroren abonnement: {bevroren.title()}")
print(f"Aantal beschikbare faciliteiten: {len(beschikbare_faciliteiten)}")
print(f"Totaal aantal trainingsuren in de week: {sum(trainingsuren)}")
print(f"Gemiddelde trainingsuren in de week: {gemiddelde_uren}")
print(f"Hoogst aantal trainingsuren op een dag: {max(trainingsuren)}")
print()
print(lijn)