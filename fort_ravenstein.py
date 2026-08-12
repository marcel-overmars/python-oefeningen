# ==========================
# Dictionary van het fort
# ==========================

fort ={
    'naam': 'fort ravenstein',
    'levenspunten': 100,
    'verdediging': 70,
    'goud': 300,
    'status': 'veilig',
}

print(fort)
print()

# ====================
# De eerste aanval
# ====================

fort['levenspunten'] = 75
fort['verdediging'] = 55
fort['status'] = 'aangevallen'

print(fort)
print()

# =======================
# Reactie op de schade
# =======================

if fort['levenspunten'] < 25:
    print("Het fort staat op instorten")
elif fort['levenspunten'] < 50:
    print("Het fort is zwaar beschadigd")
elif fort['levenspunten'] < 80:
    print("Het fort heeft schade opgelopen")
elif fort['levenspunten'] >= 80:
    print("Het fort is nog in goede staat")
print()

# ======================
# Versterking kopen
# ======================

if fort['goud'] < 100:
    versterking = 5
elif fort['goud'] < 200:
    versterking = 15
else:
    versterking = 25
print()

fort['goud'] = fort['goud'] - 100

fort['verdediging'] = fort['verdediging'] + versterking

# ==========================
# Beschikbare verdediging
# ==========================

beschikbare_verdediging =[
    'boogschutters',
    'katapult',
    'ridders',
    'kokende olie',
    'kruisboogschutters',
]

aangevraagde_verdediging =[
    'ridders',
    'kanon',
    'boogschutters',
    'draken',
]

for verdediging in aangevraagde_verdediging:
    if verdediging in beschikbare_verdediging:
        print(f"{verdediging.title()} wordt naar de muren gestuurd")
    else:
        print(f"{verdediging.title()} is niet beschikbaar")
print()

# =================
# Tweede aanval
# =================

fort['levenspunten'] = fort['levenspunten'] - 30

fort['verdediging'] = fort['verdediging'] - 20

if fort['levenspunten'] < 25:
    print("Het fort staat op instorten")
elif fort['levenspunten'] < 50:
    print("Het fort is zwaar beschadigd")
elif fort['levenspunten'] < 80:
    print("Het fort heeft schade opgelopen")
elif fort['levenspunten'] >= 80:
    print("Het fort is nog in goede staat")
print()

# ===============
# Eindrapport
# ===============

print("===================================")
print("=== FORT RAVENSTEIN EINDRAPPORT ===")
print("===================================")
print()
print(f"Naam: {fort['naam'].title()}")
print(f"Status: {fort['status']}")
print(f"Levenspunten: {fort['levenspunten']}")
print(f"Verdediging: {fort['verdediging']}")
print(f"Goud: {fort['goud']}")
print(f"Aantal beschikbare verdedigingseenheden: {len(beschikbare_verdediging)}")
print()