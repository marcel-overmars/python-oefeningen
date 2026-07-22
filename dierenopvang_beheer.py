# ============================================================
# PROJECT: DIERENOPVANG BEHEER
# ============================================================
#
# In dit oefenproject maak ik een eenvoudig beheersysteem voor
# een dierenopvang. De beschikbare dieren worden opgeslagen in
# een lijst, waarna verschillende wijzigingen worden uitgevoerd.
# Vervolgens wordt een dier geadopteerd, worden alle dieren
# gecontroleerd, worden de dieren gesorteerd en wordt de
# mogelijke omzet van de dierenopvang berekend. Tot slot oefen
# ik met de range()-functie om reeksen van getallen te genereren.
#
# In dit project oefen ik met:
# - Lists maken en gebruiken
# - Een lege list vullen met append()
# - Elementen wijzigen met een index
# - Nieuwe elementen invoegen met insert()
# - Elementen verwijderen met del
# - Elementen verwijderen op naam met remove()
# - Elementen verwijderen en bewaren met pop()
# - Het aantal elementen bepalen met len()
# - Strings opschonen met strip()
# - Tekst aan het begin verwijderen met removeprefix()
# - Tekst aan het einde verwijderen met removesuffix()
# - Tekst aanpassen met replace()
# - Tekst netjes weergeven met title()
# - Tijdelijk sorteren met sorted()
# - Permanent sorteren met sort()
# - Permanent sorteren in omgekeerde volgorde met reverse=True
# - For-loops gebruiken om meerdere dieren te verwerken
# - Meerdere opdrachten uitvoeren binnen één for-loop
# - Code uitvoeren nadat een for-loop is afgelopen
# - De range()-functie gebruiken om reeksen van getallen te maken
# - Variabelen gebruiken
# - Constanten gebruiken
# - Berekeningen uitvoeren
# - F-strings gebruiken
# - Geldbedragen weergeven met twee decimalen (:.2f)
# - Mijn programma overzichtelijk indelen met commentaarblokken
#
# Doel:
# In dit project combineer ik vrijwel alle onderwerpen die ik
# tot nu toe heb geleerd. Ik oefen opnieuw met lists,
# stringmethodes, for-loops, sorteren en berekeningen. Daarnaast
# leer ik hoe de range()-functie werkt en dat de eindwaarde van
# range() niet wordt meegenomen.
# ============================================================


print("===========================")
print("=== Dierenopvang beheer ===")
print("===========================")
print()

# =================================
# Lijst van te adopteren dieren
# =================================

dieren = []
dieren.append(' IMG_hond_max.png')
dieren.append('IMG_kat_luna.png ')
dieren.append(' IMG_konijn_frummel.png ')
dieren.append(' IMG_hond_rex.png')
dieren.append('IMG_kat_fina.png ')
dieren.append(' IMG_konijn_knabbel.png ')
dieren.append(' IMG_hond_pip.png')
dieren.append('IMG_kat_tijger.png ')
print(dieren)
print()

# ====================================
# Wijzigingen in beschikbare dieren
# ====================================

del dieren[-1]
dieren.remove(' IMG_konijn_frummel.png ')
dieren[0] = ' IMG_hond_beer.png'
dieren.insert(1, ' IMG_konijn_stamper.png ')
print(dieren)
print()

# ===================
# Geadopteerd dier
# ===================

geadopteerd =(
    dieren
        .pop(3)
        .strip()
        .removeprefix('IMG_')
        .removesuffix('.png')
        .title()
        .replace("_", " ")
)
print(f"{geadopteerd} is geadopteerd en dus niet meer beschikbaar!")
print()

# =================================
# Aantal dieren nog beschikbaar
# =================================

beschikbaar = len(dieren)
print(f"Het aantal nog beschikbare dieren: {beschikbaar}")
print()

# ================================
# Bericht bij alle dieren
# ================================

for dier in dieren:
    nieuw_dier =(
        dier
            .strip()
            .removeprefix("IMG_")
            .removesuffix(".png")
            .replace("_", " ")
            .title()
    )
    print(f"{nieuw_dier} kan goed met kinderen!")
    print(f"{nieuw_dier} houdt van aandacht!\n")
print("Al onze dieren zijn gecontroleerd door onze dierenarts!")

# ============================
# Controle van de dieren
# ============================

for dier in dieren:
    nieuw_dier =(
        dier
            .strip()
            .removeprefix("IMG_")
            .removesuffix(".png")
            .replace("_", " ")
            .title()
    )
    print(f"{nieuw_dier} heeft recent een controle gehad!\n")

# ===============================================
# Tijdelijke en permanent gesorteerde volgorde
# ===============================================

print("Hieronder staat de tijdelijk gesorteerde alfabetische volgorde:")
print(sorted(dieren))
print()
dieren.sort()
print("Hieronder staat de permanent alfabetisch gesorteerde volgorde:")
print(dieren)
print()
dieren.sort(reverse=True)
print("Hieronder staat de permanent omgekeerde alfabetisch gesorteerde volgorde:")
print(dieren)
print()

# ==================
# Adoptie kosten
# ==================

ADOPTIE_KOSTEN = 45
aantal_honden = 37
aantal_katten = 32
aantal_konijnen = 16
KORTING = 10
print("Adoptie kosten bedragen €45.00, op konijnen krijgt u €10.00 korting.")
print()

totaal_honden = aantal_honden * ADOPTIE_KOSTEN
totaal_katten = aantal_katten * ADOPTIE_KOSTEN
konijnen_zonder_korting = aantal_konijnen * ADOPTIE_KOSTEN
korting_konijnen = aantal_konijnen * KORTING
totaal_konijnen = konijnen_zonder_korting - korting_konijnen
totale_omzet = totaal_honden + totaal_katten + totaal_konijnen
print(f"De totale omzet als alle dieren geadopteerd worden bedraagt €{totale_omzet:.2f}")
print()

# =================
# oefening range
# =================

for waarde in range(1, 11):
    print(waarde)
print()

for waarde in range(5, 16):
    print(waarde)
print()

for waarde in range(11):
    print(waarde)