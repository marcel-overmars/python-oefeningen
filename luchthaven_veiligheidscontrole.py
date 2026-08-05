# ==========================================================
# Uitleg project: Luchthaven Veiligheidssysteem
# ==========================================================
#
# In dit project heb ik geoefend met verschillende onderdelen
# van Python die ik tot nu toe heb geleerd.
#
# Ik begin met een tuple waarin de vaste luchthavenzones
# worden opgeslagen. Omdat deze zones niet veranderen tijdens
# het programma, is een tuple hiervoor geschikt.
#
# Daarna maak ik een lijst met verbannen reizigers en een lijst
# met toegestane bestemmingen. Met de operators 'in' en
# 'not in' controleer ik of een bestemming is toegestaan en
# of een reiziger niet op de lijst met verbannen personen staat.
#
# Vervolgens maak ik gegevens aan voor twee reizigers.
# Met if-statements controleer ik:
# - of iemand een eersteklas ticket heeft;
# - of de gekozen bestemming is toegestaan;
# - of de reiziger mag vliegen.
#
# Daarna werk ik met een lijst van medewerkers.
# Ik oefen met:
# - append() om een medewerker toe te voegen;
# - pop() om medewerkers te verwijderen en hun naam op te slaan;
# - het wijzigen van een bestaand item in een lijst.
#
# Vervolgens maak ik met een for-loop en range() een lijst
# met controleaantallen per uur. Met append() voeg ik deze
# waarden toe aan de lijst.
#
# Daarna gebruik ik verschillende functies om gegevens uit
# de lijst te halen:
# - len() om het aantal meetmomenten te bepalen;
# - min() voor het laagste aantal controles;
# - max() voor het hoogste aantal controles;
# - sum() voor het totaal aantal gecontroleerde reizigers.
#
# Ook oefen ik met slices door de eerste drie en de laatste
# drie meetmomenten uit de lijst weer te geven.
#
# Tot slot maak ik een overzichtelijk eindrapport waarin de
# belangrijkste gegevens van het programma worden samengevat.
#
# Met dit project heb ik geoefend met:
# - tuples
# - lists
# - append()
# - pop()
# - variabelen
# - if / else
# - and
# - in / not in
# - for-loops
# - range()
# - slices
# - len()
# - min()
# - max()
# - sum()
# - f-strings
# - nette indeling van een Python-programma
# ==========================================================

lijn = "================================================"

# ===========================
# Vaste luchthavenzones
# ===========================

luchthavenzones =(
    'vertrekhal',
    'aankomsthal',
    'douane',
    'bagagecontrole',
    'personeelsruimte',
    'VIP-lounge',
)

# ======================
# Reizigerscontrole
# ======================

verbannen_reizigers = ['marcel', 'bianca', 'lucy',]
toegestane_bestemmingen = ['londen', 'brussel', 'rome',]

naam_1 = 'lucy'
leeftijd_1 = 33
ticket_1 = 'eerste klas'
bestemming_1 = 'brussel'

naam_2 = 'kevin'
leeftijd_2 = 25
ticket_2 = 'tweede klas'
bestemming_2 = 'madrid'

if ticket_1 == 'eerste klas':
    print(f"Welkom in de VIP-lounge {naam_1}.")
else:
    print("U heeft niet de juiste ticketsoort.")
print()

if bestemming_1 in toegestane_bestemmingen:
    print("U kunt uw reis vervolgen")
else:
    print("De reis is geannuleerd, u kunt niet verder.")
print()

if naam_1 not in verbannen_reizigers:
    print("Wij wensen u een fijne vlucht.")
else:
    print("Volgens het systeem mag u niet naar het buitenland vliegen.")
print()
print(lijn)
print()

if ticket_2 == 'eerste klas':
    print(f"Welkom in de VIP-lounge {naam_2}.")
else:
    print("U heeft niet de juiste ticketsoort.")
print()

if bestemming_2 in toegestane_bestemmingen:
    print("U kunt uw reis vervolgen.")
else:
    print("De reis is geannuleerd, u kunt niet verder.")
print()

if naam_2 not in verbannen_reizigers:
    print("Wij wensen u een fijne vlucht.")
else:
    print("Volgens het systeem mag u niet naar het buitenland vliegen")
print()
print(lijn)
print()

# ==================================
# Lijst medewerkers en wijzigingen
# ==================================

medewerkers =[
    'harry',
    'alissa',
    'leon',
    'edwin',
    'daan',
    'eric',
    'ron',
    'nikki',
]

medewerkers[0] = 'harm'
ziek = medewerkers.pop(-1)
controlepost = medewerkers.pop(2)
medewerkers.append('stacy')

print("Lijst van actuele medewerkers:")
print(medewerkers)
print()
print(f"De volgende medewerker is ziek: {ziek.title()}")
print(f"{ziek.title()} wordt vervangen door {medewerkers[-1].title()}.")
print(f"{controlepost.title()} is tijdelijk overgeplaatst naar de controlepost.")
print()
print(lijn)
print()

# ===============================
# Drukte bij de controleposten
# ===============================

controles = []

for uur in range(1, 8):
    controle = uur * 20
    controles.append(controle)

print(f"Alle aantallen gecontroleerden per uur: {controles}\n")
print(f"Aantallen gecontroleerd de eerste 3 uur: {controles[:3]}\n")
print(f"Aantallen gecontroleerd de laatste 3 uur: {controles[-3:]}\n")
print(f"Het rustigste uur met controles: {min(controles)}\n")
print(f"Het drukste uur met controles: {max(controles)}\n")
print(f"Het totaal aantal gecontroleerde reizigers: {sum(controles)}\n")
print(f"Het aantal gemeten uren: {len(controles)}\n")
print(lijn)
print()

# ===================
# Eindrapport
# ===================

print("=====================================")
print("=== LUCHTHAVEN VEILIGHEIDSRAPPORT ===")
print("=====================================")
print()
print(f"Aantal luchthavenzones: {len(luchthavenzones)}")
print(f"Aantal actieve medewerkers: {len(medewerkers)}")
print(f"Zieke medewerker: {ziek.title()}")
print(f"Overgeplaatste medewerker: {controlepost.title()}")
print(f"Aantal toegestane bestemmingen: {len(toegestane_bestemmingen)}")
print(f"Aantal gemeten uren: {len(controles)}")
print(f"Laagste aantal controles in een uur: {min(controles)}")
print(f"Hoogste aantal controles in een uur: {max(controles)}")
print(f"Totaal aantal gecontroleerde reizigers: {sum(controles)}")
print()
print(lijn)