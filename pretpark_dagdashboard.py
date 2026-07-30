# ============================================================
# PROJECT: PRETPARK DAGDASHBOARD
# ============================================================
#
# In dit project maak ik een uitgebreid beheersysteem voor een
# pretpark. Het programma houdt verschillende onderdelen van
# een openingsdag bij, zoals attracties, onderhoud,
# bezoekersaantallen, inkomsten en medewerkers. Aan het einde
# van het programma wordt een overzichtelijk dagdashboard
# weergegeven met belangrijke statistieken.
#
# In dit project oefen ik met:
# - Lijsten maken en beheren
# - Gegevens toevoegen, wijzigen en verwijderen
# - Werken met indexen
# - Een lijst kopiëren met [:]
# - For-loops gebruiken
# - range() gebruiken
# - Automatisch lijsten opbouwen
# - List comprehensions gebruiken
# - Slices gebruiken om delen van lijsten te selecteren
# - min(), max(), sum() en len() gebruiken
# - F-strings gebruiken
# - Geldbedragen weergeven met twee decimalen
# - Overzichtelijke uitvoer maken met duidelijke
#   commentaarblokken
#
# Doel:
# Met dit project combineer ik vrijwel alle Python-onderwerpen
# die ik tot nu toe heb geleerd in één groter programma.
# Ik laat zien hoe verschillende lijsten samen kunnen werken
# binnen één toepassing en hoe gegevens overzichtelijk kunnen
# worden verwerkt en weergegeven in een einddashboard.
#
# Tijdens het bouwen heb ik onder andere geleerd:
# - wanneer een kopie van een lijst nodig is;
# - hoe slices gebruikt kunnen worden om gegevens te verdelen;
# - hoe automatisch gegenereerde gegevens kunnen worden
#   samengevat met statistische functies;
# - hoe een groter programma overzichtelijk blijft door het op
#   te delen in duidelijke onderdelen met commentaarblokken.
# ============================================================

print("===========================")
print("== Pretpark dagdashboard ==")
print("===========================")
print()

# =========================
# Lijst van de attracties
# =========================

attracties = []
attracties.append('yoy chill')
attracties.append('eat my dust')
attracties.append('draka')
attracties.append('speed of sound')
attracties.append('untamed')
attracties.append('lost gravity')
attracties.append('condor')
attracties.append('goliath')
attracties.append('crazy river')
attracties.append('splash battle')
attracties.append('cooldown')
attracties.append('spinning vibe')
attracties.append('los sombreros')
attracties.append('super swing')
attracties.append('wind seekers')

# =============================
# Wijzigingen bij attracties
# =============================

attracties.insert(3, 'bubble swirl')
del attracties[5]
attracties[1] = 'garage'
defect = attracties.pop(-3)
print(f"{defect.title()} is de komende weken gesloten door een defect!")
print()
print("==========================")
print("== Lijst van attracties ==")
print("==========================")
print()
for attractie in attracties:
    print(f"\t{attractie.title()}")
print()
print("==========================")
print()

# =================================
# Kopie voor de onderhoudsdienst
# =================================

attracties_2 = attracties[:]
attracties_2.append('mini taxi')
attracties_2.append('stunt flight')
attracties_2.remove('speed of sound')
attracties_2[0] = 'space kidz'

# ============================================================
# Zowel de gewone lijst als de onderhoudslijst onder elkaar
# ============================================================

print("============================")
print("=== Lijst van attracties ===")
print("============================")
print()
for attractie in attracties[0:]:
    print(f"\t{attractie.title()}")
print()
print("============================")
print()

print("============================")
print("=== Lijst van attracties ===")
print("===      onderhoud       ===")
print("============================")
print()
for onderhoud in attracties_2:
    print(f"\t{onderhoud.title()}")
print()
print("============================")
print()

# =============================
# Bezoekersaantal over 12 uur
# =============================

bezoekersaantal = []
for uren in range(1, 13):
    bezoekers = uren * 20
    bezoekersaantal.append(bezoekers)

# ================================================
# Verkorte schrijfwijze bezoekersaantal oefening
# ================================================

aantal_bezoekers = [bezoekers * 20 for bezoekers in range(1, 13)]

# =================================
# Bezoekersaantallen samenvatting
# =================================

print(f"Alle bezoekersaantallen: {(bezoekersaantal)}")
print(f"Bezoekersaantal de eerste 4 uur: {(bezoekersaantal[:4])}")
print(f"Bezoekersaantal de middelste 4 uur: {(bezoekersaantal[4:8])}")
print(f"Bezoekersaantal de laatste 4 uur: {(bezoekersaantal[-4:])}")
print(f"Het laagste bezoekersaantal is: {min(bezoekersaantal)}")
print(f"Het hoogste bezoekersaantal is: {max(bezoekersaantal)}")
print(f"Het totale aantal bezoekers: {sum(bezoekersaantal)}")
print(f"Het aantal gemeten uren: {len(bezoekersaantal)}")
print()

# ======================
# Inkomsten per uur
# ======================

inkomsten = []
for uren in range(1, 13):
    totale_inkomsten = uren * 165
    inkomsten.append(totale_inkomsten)

print(f"De inkomsten per uur zijn: {inkomsten}")
print()

print(f"De inkomsten in de ochtend zijn: {inkomsten[:4]}")
print(f"De inkomsten in de middag zijn: {inkomsten[4:8]}")
print(f"Inkomsten aan het einde van de dag zijn: {inkomsten[-4:]}")
print(f"De laagste inkomsten zijn: €{min(inkomsten):.2f}")
print(f"De hoogste inkomsten zijn: €{max(inkomsten):.2f}")
print(f"De totale inkomsten zijn: €{sum(inkomsten):.2f}")
print()

# =======================
# Lijst van medewerkers
# =======================

medewerkers = []
medewerkers.append('marcel')
medewerkers.append('martijn')
medewerkers.append('dennis')
medewerkers.append('bianca')
medewerkers.append('sander')
medewerkers.append('iris')
medewerkers.append('alice')
medewerkers.append('floris')
medewerkers.append('peter')
medewerkers.append('ronald')

medewerkers[1] = 'brit'
medewerkers.insert(-1, 'noor')
afscheid = medewerkers.pop(4)
print(f"We wensen je veel succes bij je nieuwe baan {afscheid.title()}")
print()

print("===========================")
print("== Medewerkers in dienst ==")
print("===========================")
for medewerker in medewerkers:
    print(f"==\t{medewerker.title()}\t\t ==")
print("===========================")
print()

# =================
# Werkverdeling
# =================

print("====================================")
print("\t  Ochtenddienst")
print("====================================")
print()

for ochtend in medewerkers[:4]:
    print(f"{ochtend.title()} werkt deze week in de ochtend!\n")
print("====================================")
print()

print("====================================")
print("\t    Middagdienst")
print("====================================")
print()

for middag in medewerkers[4:7]:
    print(f"{middag.title()} werkt deze week in de middag!\n")
print("====================================")
print()

print("====================================")
print("\t    Avonddienst")
print("====================================")
print()

for avond in medewerkers[7:]:
    print(f"{avond.title()} werkt deze week in de avond!\n")
print("====================================")
print()

# =====================
# Attractiestatus
# =====================

for attractie in attracties[:7]:
    print(f"De volgende attractie is geopend: {attractie.title()}\n")

for controle in attracties[7:11]:
    print(f"De volgende attractie word gecontroleerd voor onderhoud: {controle.title()}\n")

for sluit_eerder in attracties[-3:]:
    print(f"De volgende attractie zal een uur eerder sluiten: {sluit_eerder.title()}\n")

    # =================
    # Einddashboard
    # =================

    print("=============================")
    print("=== DAGOVERZICHT PRETPARK ===")
    print("=============================")
    print()
    print(f"Aantal geopende attracties: {len(attracties[:7])}")
    print(f"Aantal medewerkers: {len(medewerkers)}")
    print(f"Aantal gemeten openingsuren: {len(bezoekersaantal)}")
    print(f"Totaal aantal bezoekers: {sum(bezoekersaantal)}")
    print(f"Hoogste bezoekersaantal in een uur: {max(bezoekersaantal)}")
    print(f"Laagste bezoekersaantal in een uur: {min(bezoekersaantal)}")
    print(f"Totale dagomzet: €{sum(inkomsten):.2f}")
    print(f"Hoogste omzet in 1 uur: €{max(inkomsten):.2f}")
    print(f"Aantal attracties in het onderhoudsoverzicht: {len(attracties_2)}")
    print()
    print("=============================")