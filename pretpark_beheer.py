# ============================================================
# PROJECT: PRETPARK BEHEER
# ============================================================
#
# In dit oefenproject maak ik een eenvoudig programma voor het
# beheren van een pretpark. De attracties worden opgeslagen in
# een lijst, waarna verschillende wijzigingen worden uitgevoerd.
# Vervolgens wordt een attractie tijdelijk gesloten voor
# onderhoud, worden bezoekers geïnformeerd en worden alle
# attracties gecontroleerd. Tot slot worden de attracties
# gesorteerd en wordt de totale omzet van het pretpark berekend.
#
# In dit project oefen ik met:
# - Lists maken en gebruiken
# - Een lege list vullen met append()
# - Elementen wijzigen met een index
# - Nieuwe elementen invoegen met insert()
# - Elementen verwijderen met del
# - Elementen verwijderen en bewaren met pop()
# - Elementen verwijderen op naam met remove()
# - Het aantal elementen bepalen met len()
# - Strings opschonen met strip()
# - Tekst aan het begin verwijderen met removeprefix()
# - Tekst aan het einde verwijderen met removesuffix()
# - Tekst aanpassen met replace()
# - Tekst netjes weergeven met title()
# - Tijdelijk sorteren met sorted()
# - Permanent sorteren met sort()
# - Permanent sorteren in omgekeerde volgorde met reverse=True
# - Meerdere for-loops gebruiken
# - Meerdere opdrachten uitvoeren binnen één for-loop
# - Code uitvoeren nadat een for-loop is afgelopen
# - Variabelen
# - Constanten
# - Integers en floats
# - Berekeningen uitvoeren
# - F-strings gebruiken
# - Geldbedragen weergeven met twee decimalen (:.2f)
# - Mijn programma overzichtelijk indelen met commentaarblokken
#
# Doel:
# Leren hoe meerdere Python-onderwerpen gecombineerd kunnen
# worden binnen één groter programma. Daarnaast oefen ik met het
# verwerken van gegevens in een for-loop, het opschonen van
# strings, het sorteren van lijsten en het uitvoeren van
# berekeningen. Door alle eerder geleerde onderwerpen opnieuw te
# gebruiken, blijft de basiskennis beter hangen.
# ============================================================

print("=======================")
print("=== Pretpark beheer ===")
print("=======================")

# =========================
# Lijst van attracties
# =========================

attracties = []
attracties.append(' IMG_de_achtbaan.png')
attracties.append('IMG_het_spookhuis.png ')
attracties.append(' IMG_de_slingshot.png ')
attracties.append(' IMG_de_python.png')
attracties.append('IMG_the_flying_dutchman.png ')
attracties.append(' IMG_hoogmoed.png ')
attracties.append(' IMG_het_spiegelpaleis.png')
attracties.append('IMG_symbolica.png')
print(attracties)
print()

# ============================
# Wijzigingen in attracties
# ============================

attracties.remove('IMG_symbolica.png')
del attracties[3]
attracties.insert(2, ' IMG_de_piranha.png')
attracties[-2] = ' IMG_het_reuzenrad.png '
print(attracties)

# ==========================
# gesloten voor onderhoud
# ==========================

onderhoud = (
    attracties.pop(1)
    .strip()
    .removeprefix('IMG_')
    .removesuffix('.png')
    .replace('_', ' ')
)
print(f"{onderhoud.title()} is momenteel gesloten voor onderhoud!")
print()

# ===============================
# Aantal beschikbare attracties
# ===============================

beschikbaar = len(attracties)
print(f"Het aantal nog te gebruiken attracties is: {beschikbaar}")

for attractie in attracties:
    attractie = attractie.strip().removeprefix('IMG_').removesuffix('.png').replace("_", " ").title()
    print(f"Houd u alstublieft aan de voorschriften in {attractie}")
    print(f"Verder wensen wij u een onvergetelijke ervaring in {attractie}\n")
print("We hopen dat jullie genoten hebben van het avontuur in ons prachtige park!")
print()

# ========================
# Onderhoud uitgevoerd
# ========================

for attractie in attracties:
    attractie = attractie.strip().removeprefix('IMG_').removesuffix('.png').replace("_", " ").title()
    print(f"Het onderhoud aan {attractie} is uitgevoerd!\n")

# ===============================================
# tijdelijke en permanente gesorteerde lijsten
# ===============================================

print(sorted(attracties))
print()

attracties.sort()
print("Hieronder staat de permanent alfabetische volgorde:")
print(attracties)
print()
attracties.sort(reverse=True)
print("Hieronder staat de permanente omgekeerde alfabetische volgorde:")
print(attracties)
print()

# ====================
# Omzet berekening
# ====================

ENTREE = 35
KORTING = 0.50
aantal_volwassenen = 129
aantal_kinderen = 68
aantal_senioren = 57
print("Een kaartje kost €35.00, kinderen en senioren krijgen 50% korting")
print()

totaal_volwassenen = aantal_volwassenen * ENTREE
kinderen_zonder_korting = aantal_kinderen * ENTREE
kinderen_met_korting = kinderen_zonder_korting * KORTING
senioren_zonder_korting = aantal_senioren * ENTREE
senioren_met_korting = senioren_zonder_korting * KORTING
totale_omzet = totaal_volwassenen + kinderen_met_korting + senioren_met_korting
print(f"Er is een totale omzet gemaakt van €{totale_omzet:.2f}")