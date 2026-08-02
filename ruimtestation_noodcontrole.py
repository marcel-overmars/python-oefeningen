# ============================================================
# PROJECT: RUIMTESTATION NOODCONTROLE
# ============================================================
#
# In dit project maak ik een beheersysteem voor een
# ruimtestation dat na een botsing met ruimtepuin wordt
# gecontroleerd. Het programma geeft een overzicht van de
# afdelingen, de bemanning, de voorraden en de
# zuurstofmetingen. Daarnaast leert het programma met behulp
# van if-statements verschillende situaties op een andere
# manier te behandelen.
#
# In dit project oefen ik met:
# - Tuples voor vaste gegevens
# - Lijsten maken en aanpassen
# - append(), insert() en pop()
# - For-loops
# - If- en else-statements
# - Vergelijken met == en !=
# - Werken met hoofdletters en kleine letters bij
#   vergelijkingen
# - len(), min(), max() en sum()
# - Slices gebruiken om delen van een lijst weer te geven
# - Gegevens overzichtelijk tonen met f-strings
# - Programma's opdelen met duidelijke commentaarblokken
#
# Doel:
# Met dit project leer ik hoe een programma verschillende
# beslissingen kan nemen op basis van de gegevens die het
# verwerkt. Niet iedere afdeling, voorraad of medewerker krijgt
# dezelfde behandeling; het programma controleert eerst of een
# bepaalde situatie van toepassing is en kiest daarna de juiste
# uitvoer.
#
# Tijdens het bouwen heb ik geleerd:
# - Dat == wordt gebruikt om te controleren of twee waarden
#   gelijk zijn.
# - Dat != wordt gebruikt om te controleren of twee waarden
#   niet gelijk zijn.
# - Dat if-statements vaak samen met for-loops worden gebruikt
#   om ieder onderdeel uit een lijst afzonderlijk te
#   controleren.
# - Dat ik meerdere technieken uit eerdere hoofdstukken kan
#   combineren in één groter en logisch opgebouwd programma.
# ============================================================

# ==================================
# Vaste afdelingen ruimtestation
# ==================================

afdelingen =(
    'Commandocentrum',
    'Machinekamer',
    'Laboratorium',
    'Ziekenboeg',
    'Opslagruimte',
    'Slaapverblijf',
)

# ======================
# Lijst van bemanning
# ======================

bemanning = []

bemanning.append('mike')
bemanning.append('piet')
bemanning.append('johan')
bemanning.append('dennis')
bemanning.append('brit')
bemanning.append('sarah')
bemanning.append('noor')
bemanning.append('marcel')

# ========================
# Wijzigingen bemanning
# ========================

bemanning[0] = 'joris'
bemanning.insert(2, 'karlijn')
ziek = bemanning.pop(-1)
overgeplaatst = bemanning.pop()

print("De huidige bemanning:")
print(bemanning)
print()
print("Er zijn 2 bemanningsleden afwezig:")
print(f"{ziek.title()} is tijdelijk afwezig vanwege ziekte.")
print("Karlijn vervangt tijdelijk het zieke bemanningslid")
print(f"{overgeplaatst.title()} is overgeplaatst.")
print()

# =============================
# Controle van de afdelingen
# =============================

for afdeling in afdelingen:
    if afdeling == 'Machinekamer':
        print(f"Deze afdeling is zwaar beschadigd: {afdeling}\n")
    else:
        print(f"Deze afdeling is niet beschadigd: {afdeling}\n")
print("======================================")
print()

for afdeling in afdelingen:
    if afdeling != 'Opslagruimte':
        print(f"De volgende afdeling is toegankelijk: {afdeling}\n")
    else:
        print(f"De volgende afdeling is niet toegankelijk: {afdeling}\n")
print("======================================")
print()

# =============
# Voorraad
# =============

voorraden =(
    'zuurstofcilinders',
    'drinkwater',
    'voedselpakketten',
    'medicijnen',
    'brandstofcellen',
    'reparatiemateriaal',
    'EHBO-trommels',
)

for voorraad in voorraden:
    if voorraad != 'zuurstofcilinders':
        print(f"Van het volgende artikel is nog voldoende voorraad: {voorraad}\n")
    else:
        print(f"De volgende voorraad is volledig op: {voorraad}\n")
print("===================================")
print()

# ======================
# Zuurstofmetingen
# ======================

zuurstofmeting = []

for dag in range(1, 8):
    zuurstof = dag * 10
    zuurstofmeting.append(zuurstof)

print("Alle zuurstofmetingen:")
print(zuurstofmeting)
print()
print(f"Zuurstofmeting de eerste 3 dagen: {zuurstofmeting[:3]}\n")
print(f"Zuurstofmeting de laatste 3 dagen: {zuurstofmeting[-3:]}\n")
print(f"De laagste zuurstofmeting: {min(zuurstofmeting)}\n")
print(f"De hoogste zuurstofmeting: {max(zuurstofmeting)}\n")
print(f"Het totaal van de zuurstofmetingen: {sum(zuurstofmeting)}\n")
print(f"Het aantal gemeten dagen: {len(zuurstofmeting)}\n")

# ============================
# Eindrapport ruimtestation
# ============================

print("=================================")
print("=== RUIMTESTATION EINDRAPPORT ===")
print("=================================")
print()
print(f"Aantal afdelingen: {len(afdelingen)}")
print(f"Aantal actieve bemanningsleden: {len(bemanning)}")
print(f"Ziek bemanningslid: {ziek.title()}")
print(f"Overgeplaatst bemanningslid: {overgeplaatst.title()}")
print(f"Aantal voorraden: {len(voorraden)}")
print(f"Laagste zuurstofmeting: {min(zuurstofmeting)}")
print(f"Hoogste zuurstofmeting: {max(zuurstofmeting)}")
print(f"Aantal gemeten dagen: {len(zuurstofmeting)}")
print()
print("=================================")