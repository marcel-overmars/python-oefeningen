# ==========================================================
# UITLEG PROJECT - FESTIVAL CONTROLE EINDRAPPORT
# ==========================================================
#
# In dit project heb ik hoofdstuk 5 over if-statements
# verder geoefend en meerdere onderdelen uit eerdere
# hoofdstukken opnieuw gecombineerd.
#
# Het programma controleert verschillende onderdelen van
# een festival, zoals bezoekers, festivalbandjes,
# drankvoorraad, veiligheidsproblemen en bezoekersaantallen.
#
# Ik begin met een tuple waarin de vaste festivalzones
# worden opgeslagen. Daarna loop ik met een for-loop
# door deze zones om ze op het scherm te tonen.
#
# Vervolgens maak ik een bezoekerslijst en voer ik daar
# verschillende wijzigingen in uit:
# - een bestaande bezoeker vervangen;
# - een nieuwe bezoeker toevoegen met insert();
# - een bezoeker verwijderen met pop();
# - de verwijderde bezoeker bewaren in een variabele.
#
# Bij de leeftijdscontrole gebruik ik if-elif-ketens.
# Iedere bezoeker kan maar in één leeftijdscategorie vallen,
# dus Python stopt zodra de eerste juiste voorwaarde is
# gevonden.
#
# Daarna vergelijk ik twee verzamelingen met elkaar bij de
# festivalbandjes.
#
# Ik loop door de aangevraagde festivalbandjes en controleer
# voor ieder bandje of het voorkomt tussen de beschikbare
# festivalbandjes.
#
# Als het bandje beschikbaar is, wordt dit gemeld.
# Als het bandje niet beschikbaar is, wordt een andere
# melding weergegeven.
#
# Hetzelfde principe gebruik ik opnieuw bij de drankvoorraad.
# Hierbij vergelijk ik de bestelde dranksoorten met de lijst
# van dranksoorten die nog beschikbaar zijn.
#
# Dit onderdeel laat zien hoe een item uit de ene lijst
# gecontroleerd kan worden tegen de inhoud van een andere
# lijst.
#
# Bij de veiligheidsproblemen gebruik ik meerdere losse
# if-statements. Hierdoor kunnen meerdere waarschuwingen
# tijdens dezelfde controle worden weergegeven.
#
# Dit verschilt van een if-elif-keten, waarbij maar één
# mogelijke uitkomst wordt uitgevoerd.
#
# Voor de bezoekersaantallen maak ik met range(), een
# for-loop en append() automatisch acht meetwaarden.
#
# Daarna analyseer ik deze gegevens met:
# - slices
# - min()
# - max()
# - sum()
# - len()
#
# Ook bereken ik het gemiddelde bezoekersaantal door het
# totale aantal bezoekers te delen door het aantal metingen.
#
# Met :.0f zorg ik ervoor dat het gemiddelde zonder cijfers
# achter de komma wordt weergegeven.
#
# Tot slot maak ik een eindrapport waarin de belangrijkste
# gegevens uit het programma worden samengevat.
#
# Met dit project heb ik geoefend met:
# - tuples
# - lists
# - indexen aanpassen
# - insert()
# - pop()
# - append()
# - variabelen
# - for-loops
# - range()
# - if
# - elif
# - else
# - meerdere losse if-statements
# - in
# - ==
# - slices
# - len()
# - min()
# - max()
# - sum()
# - gemiddelde berekenen
# - title()
# - upper()
# - f-strings
# - :.0f
#
# Dit project is volledig door mijzelf geprogrammeerd als
# oefening tijdens het leren van Python. ChatGPT heeft alleen
# geholpen met uitleg, feedback en het bedenken van de
# projectopdracht.
# ==========================================================

lijn = "======================================"

# ========================
# Vaste festivalzones
# ========================

festivalzones =(
    'hoofdpodium',
    'dance area',
    'foodcourt',
    'VIP-zone',
    'camping',
)

for festivalzone in festivalzones:
    print(festivalzone)
print()
print(lijn)
print()

# ================================
# Bezoekerslijst en wijzigingen
# ================================

bezoekers = [
    'johan',
    'max',
    'lucy',
    'lizzy',
    'kevin',
    'rick',
    'daan',
]

bezoekers[0] = 'marcel'
bezoekers.insert(3, 'sasha')
vertrokken = bezoekers.pop(-2)

print("De actuele bezoekerslijst:")
print(bezoekers)
print()
print(f"De volgende bezoeker heeft het festival vroeger verlaten: {vertrokken.title()}\n")
print(lijn)
print()

# =====================
# Leeftijdscontrole
# =====================

naam_1 = 'marcel'
leeftijd_1 = 28

naam_2 = 'sasha'
leeftijd_2 = 67

naam_3 = 'kevin'
leeftijd_3 = 15

if leeftijd_1 < 16:
    print(f"{naam_1.title()} heeft geen toegang zonder begeleiding!")
elif leeftijd_1 < 18:
    print(f"{naam_1.title()} heeft alleen toegang tot de alcoholvrije zone!")
elif leeftijd_1 < 65:
    print(f"{naam_1.title()} heeft volledig toegang!")
elif leeftijd_1 >= 65:
    print(f"{naam_1.title()} krijgt het seniorentarief!")
print()

if leeftijd_2 < 16:
    print(f"{naam_2.title()} heeft geen toegang zonder begeleiding!")
elif leeftijd_2 < 18:
    print(f"{naam_2.title()} heeft alleen toegang tot de alcoholvrije zone!")
elif leeftijd_2 < 65:
    print(f"{naam_2.title()} heeft volledig toegang!")
elif leeftijd_2 >= 65:
    print(f"{naam_2.title()} krijgt het seniorentarief!")
print()

if leeftijd_3 < 16:
    print(f"{naam_3.title()} heeft geen toegang zonder begeleiding!")
elif leeftijd_3 < 18:
    print(f"{naam_3.title()} heeft alleen toegang tot de alcoholvrije zone!")
elif leeftijd_3 <65:
    print(f"{naam_3.title()} heeft volledig toegang!")
elif leeftijd_3 >= 65:
    print(f"{naam_3.title()} krijgt het seniorentarief!")
print()
print(lijn)
print()

# ==============================
# Beschikbare festivalbandjes
# ==============================

beschikbare_festivalbandjes =(
    'dagticket',
    'weekendticket',
    'camping',
    'VIP',
    'backstage',
)

aangevraagde_festivalbandjes =[
    'dagticket',
    'VIP',
    'midweek-ticket',
    'VIP',
    'camping',
    'all-in ticket'
]

for festivalbandje in aangevraagde_festivalbandjes:
    if festivalbandje in beschikbare_festivalbandjes:
        print(f"Het volgende bandje is nog beschikbaar: {festivalbandje}")
    else:
        print(f"Het volgende bandje kan niet geleverd worden: {festivalbandje.upper()}")
print()
print(lijn)
print()

# =============================
# Beschikbare drankvoorraad
# =============================

beschikbare_dranksoorten =[
    'cola',
    'sinas',
    'bier',
    'wijn',
    'bacardi',
]

bestelde_dranksoorten =[
    'bier',
    'casus',
    'cola',
    'malibu',
    'bacardi',
    'wijn',
]

for dranksoort in bestelde_dranksoorten:
    if dranksoort in beschikbare_dranksoorten:
        print(f"De volgende dranksoort is nog beschikbaar: {dranksoort}")
    else:
        print(f"De volgende dranksoort is uitverkocht: {dranksoort.upper()}")
print()
print(lijn)
print()

# =================================
# Meerdere veiligheidsmeldingen
# =================================

veiligheidsproblemen =[
    'kapot hek',
    'stroomstoring',
    'geblokkeerde nooduitgang',
    'defecte camera',
]

for veiligheidsprobleem in veiligheidsproblemen:
    if veiligheidsprobleem == 'kapot hek':
        print(f"{veiligheidsprobleem.upper()} aan de oostkant van het terrein moet gerepareerd worden!")
    if veiligheidsprobleem == 'stroomstoring':
        print(f"Er is een lichte {veiligheidsprobleem.upper()} bij het geluid!")
    if veiligheidsprobleem == 'geblokkeerde nooduitgang':
        print(f"Zorg dat de {veiligheidsprobleem.upper()} weer vrij komt!")
    if veiligheidsprobleem == 'defecte camera':
        print(f"Er is een {veiligheidsprobleem.upper()} bij de entree!")
print()
print(lijn)
print()

bezoekersaantallen = []

for uur in range(1, 9):
    bezoekersaantal = uur * 75
    bezoekersaantallen.append(bezoekersaantal)

gemiddeld_bezoekersaantal = sum(bezoekersaantallen) / len(bezoekersaantallen)

print(f"Bezoekersaantal ieder uur: {bezoekersaantallen}")
print(f"Bezoekersaantal per uur voor de eerste 3 uur: {bezoekersaantallen[:3]}")
print(f"Bezoekersaantal per uur voor de laatste 3 uur: {bezoekersaantallen[-3:]}")
print(f"Het uur met het laagste bezoekersaantal: {min(bezoekersaantallen)}")
print(f"Het uur met het hoogste bezoekersaantal: {max(bezoekersaantallen)}")
print(f"Het totale bezoekersaantal over alle uren: {sum(bezoekersaantallen)}")
print(f"Het gemiddelde bezoekersaantal: {gemiddeld_bezoekersaantal:.0f}")
print(f"Het aantal gemeten uren: {len(bezoekersaantallen)}")
print()
print(lijn)
print()

# ===============
# Eindrapport
# ===============

print("=====================================")
print("=== FESTIVAL CONTROLE EINDRAPPORT ===")
print("=====================================")
print()
print(f"Aantal festivalzones: {len(festivalzones)}")
print(f"Aantal aanwezige bezoekers: {len(bezoekers)}")
print(f"Vertrokken bezoeker: {vertrokken.title()}")
print(f"Aantal beschikbare bandjes: {len(beschikbare_festivalbandjes)}")
print(f"Aantal beschikbare dranksoorten: {len(beschikbare_dranksoorten)}")
print(f"Laagste bezoekersaantal: {min(bezoekersaantallen)}")
print(f"Hoogste bezoekersaantal: {max(bezoekersaantallen)}")
print(f"Totaal aantal bezoekers: {sum(bezoekersaantallen)}")
print(f"Gemiddeld bezoekersaantal: {gemiddeld_bezoekersaantal:.0f}")
print()
print(lijn)