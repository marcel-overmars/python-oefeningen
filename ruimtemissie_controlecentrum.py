# ==========================================================
# UITLEG PROJECT - RUIMTEMISSIE CONTROLECENTRUM
# ==========================================================
#
# In dit project bestuur ik een ruimteschip tijdens een
# missie van twaalf dagen.
#
# Met een while-loop worden de missiedagen één voor één
# doorlopen. Iedere dag verbruikt het ruimteschip brandstof
# en verliezen de bemanningsleden energie. Met % worden op
# vaste dagen medische controles en schadegebeurtenissen
# uitgevoerd.
#
# De gegevens van de bemanning zijn opgeslagen in een
# geneste dictionary. Tijdens de missie worden waarden in
# deze dictionaries aangepast en na afloop gecontroleerd.
#
# Gebruikte onderdelen:
# - dictionaries
# - dictionary in dictionary (nesting)
# - .items()
# - while-loop
# - for-loops
# - if, elif en else
# - modulo (%)
# - += en -=
# - dictionarywaarden ophalen en wijzigen
# - f-strings
#
# Zelf geprogrammeerd als oefening tijdens het leren van
# Python. ChatGPT hielp met de projectopdracht en feedback.
# ==========================================================

# ========================
# Gegevens ruimteschip
# ========================

ruimteschip = {
    'naam': 'nova explorer',
    'bemanning': 4,
    'brandstof': 100,
    'schade': 0,
    'status': 'onderweg'
}

for gegevens, waarde in ruimteschip.items():
    print(f"{gegevens.title()}: {waarde}")
print()

# ================
# De bemanning
# ================

bemanning = {
    'marcel': {
        'functie': 'commandant',
        'energie': 100
    },

    'elena': {
        'functie': 'piloot',
        'energie': 90
    },

    'victor': {
        'functie': 'technicus',
        'energie': 85,
    },

    'sofia': {
        'functie': 'arts',
        'energie': 95
    }
}

print("=== Bemanning ===")

for bemanningslid, waarde in bemanning.items():
    print(f"\n{bemanningslid.title()} - {waarde['functie']} - Energie: {waarde['energie']}")
print()

# ==============
# De missie
# ==============

dag = 1

while dag < 13:
    ruimteschip['brandstof'] -= 5
    print(f"\n=== Missiedag {dag} ===")
    print(f"Resterend brandstof: {ruimteschip['brandstof']}")

    if dag % 3 == 0:
        print("Medische controle uitgevoerd!")

    if dag % 4 == 0:
        ruimteschip['schade'] += 5
        print("Waarschuwing: schade door ruimtestof!")

    for gegevens, waarde in bemanning.items():
        waarde['energie'] -= 2

    if ruimteschip['brandstof'] < 40:
        ruimteschip['status'] = 'lage brandstof'
    elif ruimteschip['schade'] >= 15:
        ruimteschip['status'] = 'beschadigd'
    else:
        ruimteschip['status'] = 'onderweg' 

    dag += 1
print()

# ================================
# Controle van het ruimteschip
# ================================

for gegevens, waarde in ruimteschip.items():
    print(f"{gegevens.title()}: {waarde}")
print()

# =============================
# Controle van de bemanning
# =============================

for naam, gegevens in bemanning.items():
    if gegevens['energie'] < 60:
        gegevens['status'] = 'uitgeput'
    elif gegevens['energie'] < 80:
        gegevens['status'] = 'vermoeid'
    else:
        gegevens['status'] = 'fit'
    print(f"{naam.title()}: {gegevens}")

# ================
# Eindrapport
# ================

print("=====================")
print("=== MISSIERAPPORT ===")
print("=====================")
print()
print(f"Schip: {ruimteschip['naam'].title()}")
print(f"Status: {ruimteschip['status'].title()}")
print(f"Resterende brandstof: {ruimteschip['brandstof']}")
print(f"Totale schade: {ruimteschip['schade']}")
print(f"Aantal bemanningsleden: {ruimteschip['bemanning']}")
print()
print("==========")
print("BEMANNING:")
print("==========")
print()

for naam, gegevens in bemanning.items():
    print(f"De functie van {naam.title()} is: {gegevens['functie']}")