# ============================================================
# PROJECT: SPORTSCHOOL CHALLENGE
# ============================================================
#
# In dit oefenproject maak ik een eenvoudig programma voor een
# sportschoolchallenge. Het programma genereert automatisch
# trainingsdagen, berekent het aantal herhalingen en bonuspunten
# per dag en laat verschillende overzichten zien. Daarnaast
# oefen ik met het maken van lijsten met behulp van de range()
# functie en leer ik hoe ik een for-loop kan gebruiken om een
# nieuwe lijst automatisch op te bouwen.
#
# In dit project oefen ik met:
# - list(range()) gebruiken om automatisch een lijst te maken
# - De range()-functie met een begin-, eind- en stapwaarde
# - Lege lijsten maken
# - Nieuwe waarden toevoegen met append()
# - For-loops gebruiken
# - Een nieuwe lijst opbouwen met een for-loop
# - Werken met tijdelijke variabelen
# - Rekenen met machten (**)
# - Integers gebruiken
# - Het aantal elementen bepalen met len()
# - Elementen uit een lijst ophalen met een index
# - F-strings gebruiken
# - Mijn programma overzichtelijk indelen met commentaarblokken
#
# Doel:
# In dit project leer ik hoe ik automatisch gegevens kan
# genereren in plaats van alles handmatig in een lijst te zetten.
# Ik gebruik range() om reeksen van getallen te maken en bouw
# met een for-loop stap voor stap nieuwe lijsten op. Daarnaast
# oefen ik met berekeningen, indexen en het combineren van
# meerdere lijsten binnen één programma.
# ============================================================

print("=====================")
print("Sportschool challenge")
print("=====================")
print()

# ===================================
# Lijst van dagen voor de challenge
# ===================================

dagen = list(range(1, 15))
print(dagen)

# ========================
# De even trainingsdagen
# ========================

even_dagen = list(range(2, 15, 2))
print(even_dagen)

# ============================
# Aantal herhalingen per dag
# ============================

herhalingen = []
for sets in range(1, 15):
    herhaling = sets ** 2
    herhalingen.append(herhaling)

print(herhalingen)
print()

# =================
# Bonustraining
# =================

bonustraining = []
for extra in range(1, 15):
    bonus = extra ** 3
    bonustraining.append(bonus)

print(bonustraining)
print()

# ========================
# Totalen trainingsdagen
# ========================

totale_trainingsdagen = len(dagen)
totale_even_trainingsdagen = len(even_dagen)
print(f"De totale trainingsdagen zijn: {totale_trainingsdagen}\n")
print(f"De totale even trainingsdagen zijn: {totale_even_trainingsdagen}\n")
print(f"Het hoogst aantal herhalingen is: {herhalingen[-1]}")
print()
print(f"Het hoogst aantal bonuspunten is: {bonustraining[-1]}")

# ====================
# Bericht per dag
# ====================

for herhaling in herhalingen:
    print(f"Vandaag doe je {herhaling} herhalingen!\n")