# ============================================================
# PROJECT: BIBLIOTHEEKBEHEER
# ============================================================
#
# In dit oefenproject maak ik een eenvoudig beheersysteem voor
# een bibliotheek. Het programma beheert een lijst met boeken,
# leden en uitleencijfers. Daarnaast oefen ik met het tonen van
# verschillende delen van een lijst door gebruik te maken van
# slices.
#
# In dit project oefen ik met:
# - Lijsten maken en beheren
# - Gegevens toevoegen, wijzigen en verwijderen
# - Werken met slices om een deel van een lijst te tonen
# - For-loops gebruiken
# - List comprehensions
# - Automatisch lijsten opbouwen
# - min(), max(), sum() en len()
# - F-strings gebruiken
# - Mijn programma overzichtelijk indelen met commentaarblokken
#
# Doel:
# In dit project leer ik hoe ik alleen een bepaald gedeelte van
# een lijst kan gebruiken, bijvoorbeeld de eerste, middelste of
# laatste elementen. Daarnaast herhaal ik eerder geleerde
# Python-onderwerpen zoals for-loops, list comprehensions,
# statistische functies en het beheren van lijsten binnen één
# overzichtelijk programma.
# ============================================================


print("=========================")
print("=== Bibliotheekbeheer ===")
print("=========================")
print()

# ======================
# Lijst met boeken
# ======================

boeken = []
boeken.append('de kreeftenvrouwen')
boeken.append('stille geheimen')
boeken.append('harry potter')
boeken.append('onderstroom')
boeken.append('al het blauw van de hemel')
boeken.append('gewoon estavana')
boeken.append('het geheime bos')
boeken.append('weekendje weg')
boeken.append('aan het einde van de oorlog')
boeken.append('theo in golden')
boeken.append('uit de as')
boeken.append('zomernacht')
boeken.append('yesteryear')
boeken.append('de dichter en de duivel')
boeken.append('het ultieme geheim')

# =======================
# Delen van de lijst
# =======================

print("De eerste 5 boeken van de lijst:")
print(boeken[:5])
print()
print("Boeken 5 t/m 10 van de lijst:")
print(boeken[5:10])
print()
print("Alle boeken vanaf nummer 8 van de lijst:")
print(boeken[7:])
print()
print("De eerste 10 boeken van de lijst:")
print(boeken[:10])
print()

# ================================================
# Ik gebruik een for loop voor de uitleencijfers
# ================================================

uitleencijfers = []
for cijfers in range(1, 16):
    cijfer = cijfers * 3
    uitleencijfers.append(cijfer)

print('De uitleencijfers zijn:')
print(uitleencijfers)
print()

# =========================================
# vereenvoudigde loop voor uitleencijfers
# =========================================

uitleningen = [aantal * 3 for aantal in range(1, 16)]
print(uitleningen)
print()

# =============================
# Uitleencijfers opgedeeld
# =============================

print("De eerste 5 uitleencijfers:")
print(uitleencijfers[:5])
print()
print("De middelste 5 uitleencijfers:")
print(uitleencijfers[5:10])
print()
print("De laatste 5 uitleencijfers:")
print(uitleencijfers[-5:])
print()

# =================================
# Lijst met leden + aanpassingen
# =================================

leden = []
leden.append('marcel')
leden.append('dennis')
leden.append('bianca')
leden.append('iris')
leden.append('peter')
leden.append('alice')
leden.append('dylano')
leden.append('liam')

del leden[0]
leden.insert(1, 'jayden')
leden[2] = 'allisa'

print("De eerste 4 leden tonen:")
print(leden[:4])
print()
print("De laatste 4 leden tonen:")
print(leden[-4:])
print()

# ====================================================
# Uitleencijfers minimum, maximum, totaal en aantal
# ====================================================

print(f"Laagste uitleencijfer: {min(uitleencijfers)}")
print()
print(f"Hoogste uitleencijfer: {max(uitleencijfers)}")
print()
print(f"Totaal aantal uitleningen: {sum(uitleencijfers)}")
print()
print(f"Aantal uitleencijfers: {len(uitleencijfers)}")
print()