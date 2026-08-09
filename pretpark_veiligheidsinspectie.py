# ==========================================================
# UITLEG PROJECT - PRETPARK VEILIGHEIDSINSPECTIE
# ==========================================================
#
# In dit project heb ik verder geoefend met if-statements
# en vooral met het verschil tussen losse if-statements en
# een if-elif-keten.
#
# Het programma controleert verschillende onderdelen van een
# pretpark, zoals attracties, veiligheidsvoorzieningen en
# bezoekersaantallen.
#
# Ik begin met een tuple waarin de vaste parkgebieden worden
# opgeslagen. Daarna maak ik een lijst met attracties en voer
# ik verschillende wijzigingen uit, zoals:
# - een attractie vervangen;
# - een nieuwe attractie toevoegen;
# - een attractie verwijderen met pop();
# - een verwijderde waarde bewaren in een variabele.
#
# Bij de veiligheidscontrole gebruik ik meerdere losse
# if-statements. Hierdoor kunnen meerdere problemen tegelijk
# worden gevonden en kan voor ieder probleem een aparte
# waarschuwing worden weergegeven.
#
# Dit is anders dan een if-elif-keten. Bij de attractiestatus
# gebruik ik juist if-elif, omdat iedere attractie maar één
# veiligheidsstatus tegelijk kan hebben.
#
# Hierdoor heb ik geleerd:
# - losse if-statements te gebruiken wanneer meerdere
#   voorwaarden tegelijk waar kunnen zijn;
# - if-elif te gebruiken wanneer maar één van meerdere
#   mogelijke uitkomsten gekozen moet worden;
# - dat een else altijd alleen bij de if hoort waar hij
#   direct onder staat.
#
# Bij de voorzieningen oefen ik opnieuw met:
# - in
# - not in
# - meerdere onafhankelijke if-controles
#
# Hiermee controleer ik of belangrijke veiligheidsvoorzieningen
# aanwezig zijn of ontbreken.
#
# Voor de bezoekersaantallen gebruik ik een for-loop met
# range() om automatisch gegevens voor meerdere meetmomenten
# te maken. Deze waarden sla ik op in een lijst met append().
#
# Daarna analyseer ik deze lijst met:
# - slices
# - min()
# - max()
# - sum()
# - len()
#
# Ook bereken ik opnieuw zelf een gemiddelde door het totale
# bezoekersaantal te delen door het aantal metingen.
#
# Tot slot maak ik een eindrapport waarin de belangrijkste
# gegevens van de veiligheidsinspectie worden samengevat.
#
# Met dit project heb ik geoefend met:
# - tuples
# - lists
# - append()
# - pop()
# - indexen aanpassen
# - variabelen
# - for-loops
# - range()
# - if
# - elif
# - else
# - meerdere losse if-statements
# - in
# - not in
# - ==
# - slices
# - len()
# - min()
# - max()
# - sum()
# - gemiddelde berekenen
# - title()
# - f-strings
#
# Dit project is volledig door mijzelf geprogrammeerd als
# oefening tijdens het leren van Python. ChatGPT heeft alleen
# geholpen met uitleg, feedback en het bedenken van de
# projectopdracht.
# ==========================================================

lijn = "================================"

# =====================
# Vaste parkgebieden
# =====================

parkgebieden =(
    'entreeplein',
    'kinderland',
    'waterwereld',
    'avonturenpark',
    'foodcourt',
    'achtbaanzone',
)

for parkgebied in parkgebieden:
    print(parkgebied.title())
print()
print(lijn)
print()

# ================================
# Attractielijst en wijzigingen
# ================================

attracties =[
    'condor',
    'python',
    'untamed',
    'cooldown',
    'yoy chill',
    'spinning vibe',
    'super swing',
    'speed of sound',
]

attracties[4] = 'goliath'
attracties.append('draka')
gesloten = attracties.pop(-2)
gecontroleerde_attractie = attracties.pop(0)

print("De actuele lijst van attracties:")
print(attracties)
print()
print(f"De volgende attractie is vandaag gesloten: {gesloten.title()}")
print(f"De volgende attractie wordt momenteel gecontroleerd: {gecontroleerde_attractie.title()}")
print()
print(lijn)
print()

# ======================
# Veiligheidscontrole
# ======================

controles = [
    'noodverlichting',
    'brandblussers',
    'veiligheidsbeugels',
    "camera's",
    'nooduitgangen',
    'EHBO-posten',
    'alarmsysteem',
    'hekken',
]

for onderdeel in controles:
    if onderdeel == 'brandblussers':
        print(f"De {onderdeel} krijgen de jaarlijkse controle!")
    if onderdeel == "camera's":
        print(f"Er is storing bij de {onderdeel} bij de entree!")
    if onderdeel == 'alarmsysteem':
        print(f"Het {onderdeel} bij sectie C werkt niet goed!")
print()
print(lijn)
print()

# ==================
# Attractiestatus
# ==================

attractie_1 = 'condor'
veiligheidsscore_1 = 95

attractie_2 = 'python'
veiligheidsscore_2 = 54

attractie_3 = 'goliath'
veiligheidsscore_3 = 33

if veiligheidsscore_1 <= 25:
    print(f"{attractie_1.title()} moet per direct buiten werking worden gesteld!")
elif veiligheidsscore_1 <= 50:
    print(f"{attractie_1.title()} is tijdelijk gesloten vanwege verhoogd risico!")
elif veiligheidsscore_1 <= 75:
    print(f"{attractie_1.title()} heeft extra controle nodig!")
elif veiligheidsscore_1 <= 100:
    print(f"{attractie_1.title()} kan veilig gebruikt worden, het risico is laag!")
print()

if veiligheidsscore_2 <= 25:
    print(f"{attractie_2.title()} moet per direct buiten werking worden gesteld!")
elif veiligheidsscore_2 <= 50:
    print(f"{attractie_2.title()} is tijdelijk gesloten vanwege verhoogd risico!")
elif veiligheidsscore_2 <= 75:
    print(f"{attractie_2.title()} heeft extra controle nodig!")
elif veiligheidsscore_2 <= 100:
    print(f"{attractie_2.title()} kan veilig gebruikt worden, het risico is laag!")
print()

if veiligheidsscore_3 <= 25:
    print(f"{attractie_3.title()} moet per direct buiten werking worden gesteld!")
elif veiligheidsscore_3 <= 50:
    print(f"{attractie_3.title()} is tijdelijk gesloten vanwege verhoogd risico!")
elif veiligheidsscore_3 <= 75:
    print(f"{attractie_3.title()} heeft extra controle nodig!")
elif veiligheidsscore_3 <= 100:
    print(f"{attractie_3.title()} kan veilig gebruikt worden, het risico is laag!")
print()
print(lijn)
print()

# ===========================
# Ontbrekende voorzieningen
# ===========================

aanwezige_voorzieningen =[
    'AED',
    'EHBO-post',
    'brandblussers',
    'walkie talkie',
]

if 'AED' in aanwezige_voorzieningen:
    print("Er zijn voldoende AED's!")
if 'brandblussers' in aanwezige_voorzieningen:
    print("Er zijn voldoende brandblussers!")

if 'EHBO-trommels' not in aanwezige_voorzieningen:
    print("Er zijn onvoldoende EHBO-trommels, bestel bij!")
if 'noodtelefoon' not in aanwezige_voorzieningen:
    print("Er is voldoende voorraad!")
print()
print(lijn)
print()

# =======================
# Bezoekersaantallen
# =======================

bezoekersaantallen = []

for uur in range(1, 8):
    bezoekersaantal = uur * 75
    bezoekersaantallen.append(bezoekersaantal)

gemiddelde = sum(bezoekersaantallen) / len(bezoekersaantallen)

print(f"Alle aantallen per uur: {bezoekersaantallen}")
print(f"Alle aantallen per uur de eerste 3 uur: {bezoekersaantallen[:3]}")
print(f"Alle aantallen per uur de laatste 3 uur: {bezoekersaantallen[-3:]}")
print(f"Laagste bezoekersaantal in een uur: {min(bezoekersaantallen)}")
print(f"Hoogste bezoekersaantal in een uur: {max(bezoekersaantallen)}")
print(f"Het totale bezoekersaantal over de dag: {sum(bezoekersaantallen)}")
print(f"Het gemiddelde bezoekersaantal over de dag: {gemiddelde:.0f}")
print(f"Het aantal gemeten uren over de dag: {len(bezoekersaantallen)}")
print()
print(lijn)
print()

# ================
# Eindrapport
# ================

print("===================================")
print("=== VEILIGHEIDSRAPPORT PRETPARK ===")
print("===================================")
print()
print(f"Aantal parkgebieden: {len(parkgebieden)}")
print(f"Aantal actieve attracties: {len(attracties)}")
print(f"Gesloten attractie: {gesloten.title()}")
print(f"Attractie in controle: {gecontroleerde_attractie.title()}")
print(f"Aantal gecontroleerde veiligheidsonderdelen: {len(controles)}")
print(f"Aantal bezoekersmetingen: {len(bezoekersaantallen)}")
print(f"Laagste bezoekersaantal: {min(bezoekersaantallen)}")
print(f"Hoogste bezoekersaantal: {max(bezoekersaantallen)}")
print(f"Totaal aantal bezoekers: {sum(bezoekersaantallen)}")
print(f"Gemiddeld bezoekersaantal: {gemiddelde:.0f}")
print()
print(lijn)