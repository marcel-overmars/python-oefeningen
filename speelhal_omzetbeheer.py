# ============================================================
# PROJECT: SPEELHAL OMZETBEHEER
# ============================================================
#
# In dit oefenproject maak ik een eenvoudig beheersysteem voor
# een speelhal. Het programma genereert automatisch levels,
# scores en omzetgegevens. Daarnaast beheer ik een lijst met
# spelers en laat ik verschillende statistieken van de speelhal
# zien.
#
# In dit project oefen ik met:
# - list(range()) gebruiken om automatisch lijsten te maken
# - De range()-functie
# - Lege lijsten maken
# - Nieuwe waarden toevoegen met append()
# - For-loops gebruiken
# - Nieuwe lijsten opbouwen met een for-loop
# - Tijdelijke variabelen gebruiken
# - Rekenen met vermenigvuldigen (*)
# - Lijsten aanpassen met een index
# - Elementen verwijderen met remove()
# - Elementen verwijderen en bewaren met pop()
# - Het aantal elementen bepalen met len()
# - De laagste waarde bepalen met min()
# - De hoogste waarde bepalen met max()
# - Het totaal berekenen met sum()
# - F-strings gebruiken
# - Mijn programma overzichtelijk indelen met
#   commentaarblokken
#
# Doel:
# In dit project leer ik hoe ik automatisch gegevens kan
# genereren met behulp van for-loops en range(). Daarnaast
# oefen ik met het analyseren van gegevens door statistieken
# zoals de laagste waarde, hoogste waarde en totale som te
# berekenen met de ingebouwde functies min(), max() en sum().
# Ook herhaal ik eerder geleerde technieken zoals het beheren
# van lijsten, het aanpassen van gegevens en het weergeven van
# overzichtelijke informatie aan de gebruiker.
# ============================================================


print("============================")
print("=== Speelhal omzetbeheer ===")
print("============================")
print()

# ================
# Aantal levels
# ================

levels = list(range(1, 16))
print(levels)
print()

# ===================
# Score per level
# ===================

scores = []
for score in range(1, 16):
    nieuwe_score = score * 150
    scores.append(nieuwe_score)

print("De scores per level zijn:")
print(scores)
print()

# ==================
# Omzet per speler
# ==================

omzet = []
for speler in range(1, 11):
    omzet_per_speler = speler * 7
    omzet.append(omzet_per_speler)

print("De totale omzet voor dit spel per speler is:")
print(omzet)
print()

# ==============================================
# Lijst met spelers en eventuele aanpassingen
# ==============================================

spelers = []
spelers.append('Marcel')
spelers.append('Dennis')
spelers.append('Sander')
spelers.append('Bianca')
spelers.append('Iris')
spelers.append('Alice')
spelers.append('Peter')
spelers.append('Dylano')

spelers.remove('Dylano')
spelers[0] = 'Jayden'

gestopt = spelers.pop(1)
print(f"{gestopt} speelt niet meer mee!\n")
print("De uiteindelijke lijst is:")
print(spelers)
print()

# ===========
# Scores
# ===========

laagste_score = min(scores)
hoogste_score = max(scores)
totaal_aantal_punten = sum(scores)
print(f"De laagste score is: {laagste_score}")
print(f"De hoogste score is: {hoogste_score}")
print(f"Het totale aantal punten is: {totaal_aantal_punten}")
print()

# ========
# Omzet
# ========

laagste_omzet = min(omzet)
hoogste_omzet = max(omzet)
totale_omzet = sum(omzet)
print(f"De laagste omzet is: {laagste_omzet}")
print(f"De hoogste omzet is: {hoogste_omzet}")
print(f"De totale omzet is: {totale_omzet}")
print()

# ==========================
# Aantal levels en spelers
# ==========================

aantal_levels = len(levels)
aantal_spelers = len(spelers)
print(f"Het aantal levels is: {aantal_levels}")
print(f"Het aantal spelers is: {aantal_spelers}")