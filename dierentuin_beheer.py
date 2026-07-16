print("=========================")
print("=== DIERENTUIN BEHEER ===")
print("=========================")
print()

# ===================================
# Lijst van dieren in de dierentuin
# ===================================

dieren = []
dieren.append('leeuw')
dieren.append('olifant')
dieren.append('giraffe')
dieren.append('bruine beer')
dieren.append('wolf')
dieren.append('tijger')
dieren.append('neushoorn')
dieren.append('nijlpaard')
print(dieren)
print()

# =================================
# Wijzigingen beschikbare dieren
# =================================

dieren[-1] = 'zebra'
dieren.insert(3, 'krokodil')
del dieren[2]
afwezig = dieren.pop(0)
dieren.remove('wolf')
print(f"De {afwezig.title()} is tijdelijk afwezig in de dierentuin vanwege een fokprogramma!")
print()

# ===================================
# Aantal dieren en speciale dieren
# ===================================

aantal_dieren = len(dieren)
print(f"Het aantal dieren te bezichtigen is: {aantal_dieren}")
print()
print("Bijzondere dieren die bezichtigd kunnen worden:")
print()
print(dieren[1].upper())
print(dieren[3].upper())
print(dieren[-1].upper())
print()

# =================
# Gevoerde dieren
# =================

print("=== GEVOERDE DIEREN ===")
print()

for dier in dieren:
    print(f"Het volgende dier is gevoerd:\t{dier.title()}")
print()

# ===================================
# Controle uitvoering bij de dieren
# ===================================

print("=== GECONTROLEERDE DIEREN ===")
print()

for dier in dieren:
    print(f"De controle is uitgevoerd bij de {dier.title()}!")
print()

# ===============================
# Dierenverblijven op volgorde
# ===============================

print(sorted(dieren))
print()

dieren.sort()
print(f"permanente alfabetische volgorde:")
print(dieren)
print()

dieren.sort(reverse=True)
print("permanente omgekeerde alfabetische volgorde:")
print(dieren)
print()

# ==================
# Berekening omzet
# ==================

PRIJS_TOEGANGSKAART = 35
aantal_bezoekers = 267
opbrengst_souvenirwinkel = 3_250.35
opbrengst_restaurant = 3_596.95
totale_omzet = (PRIJS_TOEGANGSKAART * aantal_bezoekers) + opbrengst_souvenirwinkel + opbrengst_restaurant
print(f"De totale omzet van de dierentuin is €{totale_omzet:.2f}")