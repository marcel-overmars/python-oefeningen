# ==========================================================
# Uitleg
# ==========================================================
#
# In dit project heb ik verder geoefend met if-statements.
# Ik heb geleerd hoe ik meerdere voorwaarden tegelijk kan
# controleren met het keyword 'and'. Een bezoeker krijgt
# bijvoorbeeld alleen toegang tot het VIP-terrein wanneer
# hij of zij minimaal 18 jaar oud is én een VIP-ticket heeft.
#
# Daarnaast heb ik opnieuw geoefend met het vergelijken van
# tekst en getallen door gebruik te maken van:
#
# - ==
# - !=
# - >=
# - <=
#
# Ook heb ik opnieuw gewerkt met tuples voor vaste gegevens,
# lijsten voor gegevens die kunnen veranderen en for-loops om
# meerdere gegevens automatisch te verwerken.
#
# Tijdens dit project heb ik opnieuw geoefend met:
#
# - tuples
# - lijsten
# - append()
# - insert()
# - pop()
# - indexen aanpassen
# - for-loops
# - if / else
# - and
# - ==
# - !=
# - >=
# - <=
# - range()
# - len()
# - min()
# - max()
# - sum()
# - slices
#
# Door oudere onderdelen opnieuw te gebruiken merk ik dat de
# basis van Python steeds beter blijft hangen. Ik hoef minder
# na te denken over de syntax en kan me steeds meer richten
# op de logica van een programma.
# ==========================================================

lijn = "============================================="

# ===========================
# Vaste festivalterreinen
# ===========================

festivalterreinen =(
    'hoofdpodium',
    'dance arena',
    'rock stage',
    'foodcourt',
    'camping',
    'VIP-terrein',
)

# ======================
# Bezoekersgegevens
# ======================

naam = 'marcel'
leeftijd = 41
ticketstatus = 'VIP'
geldbedrag = 150

naam_1 = 'dylano'
leeftijd_1 = 18
ticketstatus_1 = 'normaal'
geldbedrag_1 = 75

# ======================
# Bezoekerscontrole
# ======================

if leeftijd >= 18 and ticketstatus == 'VIP':
    print(f"Welkom op het VIP-terrein {naam_1.title()}!")
else:
    print("U heeft geen toegang tot het VIP-terrein!")
print()

if leeftijd_1 >= 18 and ticketstatus_1 =='VIP':
    print(f"Welkom op het VIP-terrein {naam.title()}!")
else:
    print("U heeft geen toegang tot het VIP-terrein!")
print()
print(lijn)
print()

# ==========================================
# Artiestenlijst en eventuele wijzigingen
# ==========================================

artiesten =[
    'linking park',
    'taylor swift',
    'eminem',
    'dotan',
    'twarres',
    'bad bunny',
    'snoopdogg',
    'jan smith',
]

afwezig = artiesten.pop(-1)
artiesten.append('shakira')
artiesten[5] = 'lady gaga'
artiesten.insert(1, 'elton john')

for artiest in artiesten:
    print(artiest)
print()
print(f"{afwezig.title()} is ziek en zal vervangen worden door {artiesten[-1].title()}")
print()
print("lijn")
print()

# ===================
# Podiumcontrole
# ===================

for festivalterrein in festivalterreinen:
    if festivalterrein == 'rock stage':
        print(f"Het volgende gebied is gesloten vanwege technische problemen: {festivalterrein.title()}\n")
    else:
        print(f"Het volgende terrein is open voor de gasten: {festivalterrein.title()}\n")
print(lijn)
print()

for festivalterrein in festivalterreinen:
    if festivalterrein != 'dance arena':
        print(f"Het volgende gebied is veilig: {festivalterrein.title()}\n")
    else:
        print(f"Het volgende gebied is extra beveiliging nodig: {festivalterrein.title()}\n")
print(lijn)
print()

# ==================
# Drankvoorraad
# ==================

bier, wijn, baco, dropshot, cola, sinas, water = 3, 8, 16, 20, 7, 5, 3

if bier >= 5 and bier <= 30:
    print("Er is voldoende bier!\n")
else:
    print("Bier bij bestellen!!\n")

if wijn >= 5 and wijn <= 30:
    print("Er is voldende wijn!\n")
else:
    print("Wijn bijbestellen!!\n")

if baco >= 5 and baco <= 30:
    print("Er is voldende baco!\n")
else:
    print("Baco bijbestellen!!\n")

if dropshot >= 5 and dropshot <= 30:
    print("Er is voldende dropshot!\n")
else:
    print("Dropshot bijbestellen!!\n")

if cola >= 5 and cola <= 30:
    print("Er is voldende cola!\n")
else:
    print("Cola bijbestellen!!\n")

if sinas >= 5 and sinas <= 30:
    print("Er is voldende sinas!\n")
else:
    print("Sinas bijbestellen!!\n")

if water >= 5 and water <= 30:
    print("Er is voldende water!\n")
else:
    print("Water bijbestellen!!\n")
print()
print(lijn)
print()

# ================================
# Dagelijkse bezoekersaantallen
# ================================

bezoekers = []

for dag in range(1, 8):
    bezoekersaantal = dag * 500
    bezoekers.append(bezoekersaantal)

print(f"Het bezoekersaantal per dag: {bezoekers}\n")
print(f"Bezoekersaantal de eerste 3 dagen: {bezoekers[:3]}\n")
print(f"Bezoekersaantal de laatste 3 dagen: {bezoekers[-3:]}\n")
print(f"Het laagste aantal bezoekers op een dag: {min(bezoekers)}\n")
print(f"Het hoogste aantal bezoekers op een dag: {max(bezoekers)}\n")
print(f"Het totaal aantal bezoekers in de week: {sum(bezoekers)}\n")
print(f"Totaal aantal gemeten dagen: {len(bezoekers)}\n")
print(lijn)
print()

# ==================
# Eindoverzicht
# ==================

print("==============================")
print("=== Festival eindoverzicht ===")
print("==============================")
print()
print(f"Aantal festivalgebieden: {len(festivalterreinen)}")
print(f"Aantal actieve artiesten: {len(artiesten)}")
print(f"Uitgevallen artiest: {afwezig.title()}")
print(f"Aantal bezoekersmetingen: {len(bezoekers)}")
print(f"Laagste bezoekersaantal: {min(bezoekers)}")
print(f"Hoogste bezoekersaantal: {max(bezoekers)}")
print(f"Totaal aantal bezoekers: {sum(bezoekers)}")
print()
print("==============================")