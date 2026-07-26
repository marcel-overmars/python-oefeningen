# ============================================================
# PROJECT: DIERENTUINBEHEER
# ============================================================
#
# In dit oefenproject maak ik een eenvoudig beheersysteem voor
# een dierentuin. Het programma beheert lijsten met dieren,
# verzorgers en bezoekersaantallen. Daarnaast oefen ik met het
# gebruiken van slices binnen een for-loop om alleen een
# specifiek gedeelte van een lijst te verwerken.
#
# In dit project oefen ik met:
# - Lijsten maken en beheren
# - Gegevens toevoegen, wijzigen en verwijderen
# - Werken met slices
# - For-loops gebruiken
# - Slices combineren met een for-loop
# - List comprehensions
# - Automatisch lijsten opbouwen
# - min(), max(), sum() en len()
# - F-strings gebruiken
# - Mijn programma overzichtelijk indelen met commentaarblokken
#
# Doel:
# In dit project leer ik hoe ik niet alleen een volledige lijst,
# maar ook een geselecteerd gedeelte van een lijst kan verwerken
# met behulp van slices in een for-loop. Daarnaast herhaal ik
# eerder geleerde Python-onderwerpen door gegevens te beheren,
# statistieken te berekenen en overzichtelijke informatie aan de
# gebruiker weer te geven.
# ============================================================


print("========================")
print("=== Dierentuinbeheer ===")
print("========================")
print()

# ===================================
# Lijst van te bezichtigen dieren
# ===================================

dieren = []
dieren.append('leeuw')
dieren.append('giraffe')
dieren.append('pinguin')
dieren.append('wolf')
dieren.append('beer')
dieren.append('tijger')
dieren.append('slang')
dieren.append('olifant')
dieren.append('neushoorn')
dieren.append('nijlpaard')
dieren.append('krokodil')
dieren.append('stokstaart')
dieren.append('reuzenpanda')
dieren.append('koala')
dieren.append('gorilla')

# ================================
# De lijst van dieren opgedeeld
# ================================

print("De eerste 5 dieren van de lijst:")
print(f"{dieren[:5]}\n")
print("De laatste 5 dieren van de lijst:")
print(f"{dieren[-5:]}\n")
print("Alle dieren vanaf nummer 8 van de lijst:")
print(f"{dieren[7:]}\n")
print(f"De dieren van 4 t/m 9 van de lijst:")
print(f"{dieren[3:9]}")
print()

# =======================================
# Lijst met verzorgers en aanpassingen
# =======================================

verzorgers = []
verzorgers.append('marcel')
verzorgers.append('dennis')
verzorgers.append('alice')
verzorgers.append('peter')
verzorgers.append('rob')
verzorgers.append('jeroen')
verzorgers.append('bianca')
verzorgers.append('iris')

verzorgers.remove('marcel')
verzorgers.insert(1, 'floris')
verzorgers.insert(-1, 'brit')
verzorgers[-2] = 'john'

afwezig = verzorgers.pop(3).title()
print(f"{afwezig} is langdurig ziek!")

# ==========================================
# Lijst met dagelijkse bezoekersaantallen
# ==========================================

bezoekersaantal = []
for dagen in range(1, 8):
    bezoekers = dagen * 50
    bezoekersaantal.append(bezoekers)

print("Het bezoekersaantal per dag is:")
print(bezoekersaantal)
print()

# =======================================
# Ter oefening de vereenvoudigde lijst
# =======================================

bezoekers_per_dag = [dagen * 50 for dagen in range(1, 8)]
print(bezoekers_per_dag)
print()

# ====================================
# De laagste en hoogste waarde etc.
# ====================================

print(f"Het laagst aantal bezoekers is: {min(bezoekersaantal)}\n")
print(f"Het hoogst aantal bezoekers is: {max(bezoekersaantal)}\n")
print(f"Het totaal aantal bezoekers over de week is: {sum(bezoekersaantal)}\n")
print(f"Dit is allemaal berekend over: {len(bezoekersaantal)} dagen")
print()

# ===============================================
# For loops met slices voor een nette weergave
# ===============================================

print("==========================")
print("==  De eerste 5 dieren  ==")
print("==========================")
for dier in dieren[:5]:
    print(f"\t{dier.title()}")
print("==========================")
print()

print("==========================")
print("== De laatste 5 dieren  ==")
print("==========================")
for dier in dieren[-5:]:
    print(f"\t{dier.title()}")
print("==========================")
print()

print("==========================")
print("= De eerste 4 verzorgers =")
print("==========================")
for verzorger in verzorgers[:4]:
    print(f"\t{verzorger.title()}")
print("==========================")
print()

print("===========================")
print("= De laatste 3 verzorgers =")
print("===========================")
for verzorger in verzorgers[-3:]:
    print(f"\t{verzorger.title()}")
print("===========================")
print()

# ==================================
# For loop voor de gevoerde dieren
# ==================================

print("===========================")
print(f"Afvinklijst gevoerde dieren")
print("===========================")
print()
for dier in dieren[:5]:
    print(f"{dier.title()} is gevoerd.\n")
for dier in dieren[5:10]:
    print(f"{dier.title()} moet nog gevoerd worden.\n")
for dier in dieren[-5:]:
    print(f"{dier.title()} is gevoerd.\n")