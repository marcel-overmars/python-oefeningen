# ==========================================================
# UITLEG PROJECT - BERGREDDING DAGOVERZICHT
# ==========================================================
#
# In dit project oefen ik verder met de basis van Python.
# Het doel was om verschillende onderwerpen uit eerdere
# hoofdstukken te combineren met de nieuwe if-elif-else
# structuur.
#
# Wat ik in dit project heb geoefend:
#
# - Een tuple gebruiken voor vaste berggebieden.
# - Een lijst maken en wijzigen met:
#       * append()
#       * pop()
#       * vervangen van een item
# - Werken met variabelen voor deelnemers, leeftijden en
#   ervaringsscores.
# - if-elif-else gebruiken om deelnemers automatisch in de
#   juiste ervaringsgroep te plaatsen:
#       * beginnersgroep
#       * gevorderdengroep
#       * expertgroep
# - Controleren of materialen aanwezig zijn met:
#       * in
#       * not in
# - Een for-loop gebruiken om ieder materiaal afzonderlijk
#   te controleren en één beschadigd materiaal een aparte
#   melding te geven.
# - Een lijst met reddingsmeldingen opbouwen met range() en
#   append().
# - Werken met slices om de eerste en laatste dagen van de
#   week weer te geven.
# - Gegevens samenvatten met:
#       * len()
#       * min()
#       * max()
#       * sum()
# - Alle informatie overzichtelijk weergeven in een
#   eindrapport.
#
# Tijdens dit project heb ik vooral geoefend met het maken
# van keuzes in een programma. Met if-elif-else kan een
# programma meerdere mogelijke uitkomsten hebben, afhankelijk
# van de ingevoerde gegevens.
# ==========================================================

lijn = "============================================="

# ======================
# Vaste berggebieden
# ======================

gebieden =(
    'dennenbos',
    'adelaarsklif',
    'gletsjerpad',
    'watervalroute',
    'berghut',
    'top van aurora',
)

for gebied in gebieden:
    print(gebied.title())
print()
print(lijn)
print()

# ======================================
# Deelnemers en wijzigingen in rooster
# ======================================

deelnemers = [
    'naomi',
    'kim',
    'joris',
    'marcus',
    'danny',
    'ben',
    'justin',
    'marcel',
]

deelnemers[2] = 'jordy'
overgeplaatst = deelnemers.pop(1)
afgemeld = deelnemers.pop(-1)
deelnemers.append('dennis')

print(deelnemers)
print()
print(f"De volgende deelnemer is overgeplaatst: {overgeplaatst.title()}")
print()
print(f"De volgende deelnemer heeft zich afgemeld: {afgemeld.title()}")
print(f"Deze deelnemer wordt vervangen door: {deelnemers[-1].title()}\n")
print(lijn)
print()

# ===============================
# Ervaringsniveau per deelnemer
# ===============================

naam_1 = 'naomi'
leeftijd_1 = 28
ervaringsscore_1 = 75

naam_2 = 'ben'
leeftijd_2 = 33
ervaringsscore_2 = 23

naam_3 = 'dennis'
leeftijd_3 = 25
ervaringsscore_3 = 42

if ervaringsscore_1 < 30:
    print(f"{naam_1.title()} zit in de beginnersgroep.")
elif ervaringsscore_1 <= 69:
    print(f"{naam_1.title()} zit in de gevorderdengroep.")
else:
    print(f"{naam_1.title()} zit in de expertgroep.")
print()

if ervaringsscore_2 < 30:
    print(f"{naam_2.title()} zit in de beginnersgroep.")
elif ervaringsscore_2 <= 69:
    print(f"{naam_2.title()} zit in de gevorderdengroep.")
else:
    print(f"{naam_2.title()} zit in de expertgroep.")
print()

if ervaringsscore_3 < 30:
    print(f"{naam_3.title()} zit in de beginnersgroep.")
elif ervaringsscore_3 <= 69:
    print(f"{naam_3.title()} zit in de gevorderdengroep.")
else:
    print(f"{naam_3.title()} zit in de expertgroep.")
print()

# ========================
# Materiaalcontrole
# ========================

materialen =[
    'klimtouw',
    'helm',
    'EHBO-set',
    'zaklamp',
    'wandelstokken',
    'nooddeken',
    'kompas',
    'drinkwater',
]

if 'klimtouw' in materialen:
    print("Het klimtouw is aanwezig.")
else:
    print("Het klimtouw is niet aanwezig.")
print()

if 'helm' in materialen:
    print("De helm is aanwezig:")
else:
    print("De helm is niet aanwezig")
print()

if 'kompas' in materialen:
    print("Het kompas is aanwezig")
else:
    print("Het kompas is niet aanwezig")
print()

if 'seinpistool' not in materialen:
    print("Het seinpistool is niet aanwezig, zorg ervoor dat het aanwezig is voor vertrek.")
else:
    print("Het seinpistool is aanwezig!")
print()
print(lijn)
print()

for materiaal in materialen:
    if materiaal == 'zaklamp':
        print(f"Het volgende materiaal is beschadigd: {materiaal}\n")
    else:
        print(f"Het volgende materiaal kan gebruikt worden: {materiaal}\n")
print(lijn)
print()

# ===============================
# Dagelijkse reddingsmeldingen
# ===============================

reddingsmeldingen = []

for dag in range(1, 8):
    meldingen = dag * 15
    reddingsmeldingen.append(meldingen)

print(f"Alle meldingen per dag: {reddingsmeldingen}")
print(f"Meldingen de eerste 3 dagen: {reddingsmeldingen[:3]}")
print(f"Meldingen de laatste 3 dagen: {reddingsmeldingen[-3:]}")
print(f"Het laagst aantal meldingen op een dag: {min(reddingsmeldingen)}")
print(f"Het hoogst aantal meldingen op een dag: {max(reddingsmeldingen)}")
print(f"Het totaal aantal meldingen in de week: {sum(reddingsmeldingen)}")
print(f"Het aantal gemeten dagen: {len(reddingsmeldingen)}")
print()

# ==============
# Eindrapport
# ==============

print("================================")
print("=== BERGREDDING DAGOVERZICHT ===")
print("================================")
print()
print(f"Aantal berggebieden: {len(gebieden)}")
print(f"Aantal actieve deelnemers: {len(deelnemers)}")
print(f"Afgemelde deelnemer: {afgemeld.title()}")
print(f"Overgeplaatste deelnemer: {overgeplaatst.title()}")
print(f"Aantal materialen: {len(materialen)}")
print(f"Laagste aantal meldingen: {min(reddingsmeldingen)}")
print(f"Hoogste aantal meldingen: {max(reddingsmeldingen)}")
print(f"Totaal aantal meldingen: {sum(reddingsmeldingen)}")
print(f"Aantal gemeten dagen: {len(reddingsmeldingen)}")
print()
print(lijn)