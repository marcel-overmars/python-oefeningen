# ============================================================
# PROJECT: ARCADE HIGHSCORE CHALLENGE
# ============================================================
#
# In dit oefenproject maak ik een eenvoudig programma voor een
# arcadegame. Het programma genereert automatisch levels,
# bonuslevels en bijbehorende scores. Daarnaast beheer ik een
# kleine spelerslijst waarin spelers kunnen worden toegevoegd,
# gewijzigd of verwijderd. Tot slot laat het programma een
# overzicht zien van de belangrijkste gegevens.
#
# In dit project oefen ik met:
# - list(range()) gebruiken om automatisch lijsten te maken
# - De range()-functie met een begin-, eind- en stapwaarde
# - Lege lijsten maken
# - Nieuwe waarden toevoegen met append()
# - For-loops gebruiken
# - Nieuwe lijsten opbouwen met een for-loop
# - Werken met tijdelijke variabelen
# - Rekenen met machten (**)
# - Lijsten wijzigen met een index
# - Elementen verwijderen met remove()
# - Elementen verwijderen en bewaren met pop()
# - Elementen verwijderen met del
# - Nieuwe elementen invoegen met insert()
# - Het aantal elementen bepalen met len()
# - Gegevens uit een lijst ophalen met een index
# - F-strings gebruiken
# - Mijn programma overzichtelijk indelen met commentaarblokken
#
# Doel:
# In dit project leer ik hoe ik automatisch gegevens kan
# genereren met behulp van de range()-functie en hoe ik met een
# for-loop stap voor stap nieuwe lijsten kan opbouwen. Daarnaast
# oefen ik opnieuw met het beheren van lijsten en het combineren
# van meerdere eerder geleerde Python-onderwerpen binnen één
# logisch programma.
# ============================================================


print("===========================")
print("Arcade Highscore Challenge")
print("===========================")
print()

# =================
# Arcade levels
# =================

levels = list(range(1, 13))
bonus_levels = list(range(3, 13, 3))
print("Hieronder staan alle levels van het spel:")
print(levels)
print()
print("Hieronder staan de bonuslevels:")
print(bonus_levels)
print()

# =========================
# Scores bij de levels
# =========================

scores = []
for score in range(1, 13):
    nieuwe_score = score ** 2
    scores.append(nieuwe_score)

print(scores)
print()

bonus_scores = []
for bonus_level in range(3, 13, 3):
    bonus_score = bonus_level ** 3
    bonus_scores.append(bonus_score)

print(bonus_scores)
print()

# ==============
# Spelerstatus
# ==============

namen = []
namen.append("marcel")
namen.append("dennis")
namen.append("jasper")
namen.append("jeroen")
namen.append("peter")
print(namen)
print()

# ========================
# Wijzigingen in spelers
# ========================

namen[1] = "jayden"
namen.remove("jasper")
del namen[-1]
namen.insert(2, "liam")
print(namen)
print()

# ===================
# Tijdelijk gestopt
# ===================

vakantie =(
    namen
        .pop(0)
        .title()
)
print(f"{vakantie} is 3 weken op vakantie!")
print()
print("De spelers die nog overblijven zijn:")
print(namen)
print()

aantal_spelers = len(namen)
print(f"Aantal nog actieve spelers: {aantal_spelers}")
print(f"Totaal aantal levels: {len(levels)}")
print(f"Het aantal bonuslevels is: {len(bonus_levels)}")
print(f"De hoogst haalbare score is: {scores[-1]}")
print(f"De hoogst haalbare bonusscore is: {bonus_scores[-1]}")