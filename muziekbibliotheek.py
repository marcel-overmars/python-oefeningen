# ============================================================
# PROJECT: MUZIEKBIBLIOTHEEK
# ============================================================
#
# In dit oefenproject maak ik een eenvoudig programma voor het
# beheren van een muziekbibliotheek. Ik voeg muzieknummers toe,
# pas de lijst aan en verwijder nummers op verschillende
# manieren. Daarnaast bereken ik de kosten van een aantal
# downloads.
#
# In dit project oefen ik met:
# - Lists maken en gebruiken
# - Een lege list vullen met append()
# - Elementen wijzigen met een index
# - Nieuwe elementen invoegen met insert()
# - Elementen verwijderen met del
# - Elementen verwijderen en tegelijkertijd bewaren met pop()
# - Een specifiek element verwijderen met remove()
# - Gegevens ophalen met positieve en negatieve indexen
# - String-methodes zoals .title(), .upper() en .lower()
# - Variabelen
# - Integers en floats
# - Een constante gebruiken
# - Rekenen met downloadprijzen en totaalbedragen
# - F-strings gebruiken
# - print(), \n en duidelijke kopjes gebruiken voor een
#   overzichtelijke uitvoer
#
# Doel:
# Leren hoe een lijst tijdens een programma kan veranderen door
# gegevens toe te voegen, te wijzigen en te verwijderen. Ook
# oefen ik met het opnieuw gebruiken van verwijderde gegevens
# en het uitvoeren van eenvoudige berekeningen binnen één
# groter oefenproject.
# ============================================================


# ===================
# beschikbare nummers
# ===================

print("=================")
print("MUZIEKBIBLIOTHEEK")
print("=================")
print()

muziekbibliotheek = []

muziekbibliotheek.append('in the end')
muziekbibliotheek.append('zombie')
muziekbibliotheek.append('easier for you')
muziekbibliotheek.append('messenger')
muziekbibliotheek.append('numb')
muziekbibliotheek.append('leave out all the rest')
muziekbibliotheek.append('somewhere i belong')
muziekbibliotheek.append('beautiful')

# =======================
# Wijzigingen muzieklijst
# =======================

muziekbibliotheek[1] = 'fighter'
muziekbibliotheek.insert(3, 'the way i am')
del muziekbibliotheek[5]
gedownload_nummer = muziekbibliotheek.pop()
verboden_nummer = 'in the end'
muziekbibliotheek.remove('in the end')
print(f"Dit nummer is tijdelijk niet beschikbaar:\t{gedownload_nummer.title()}")
print()
print(f"{verboden_nummer.upper()} is niet meer beschikbaar omdat de rechten verlopen zijn!")
print()

# =================
# Populaire nummers
# =================


print("=================")
print(f"Populaire nummers")
print("=================")
print()
print(muziekbibliotheek)
print()
print(muziekbibliotheek[3].upper())
print(muziekbibliotheek[4].title())
print(muziekbibliotheek[-1].lower())
print()

# ===============
# Download kosten
# ===============

DOWNLOAD_KOSTEN = 1.49
downloads = 4
totale_kosten = downloads * DOWNLOAD_KOSTEN
print(f"De kosten voor de 4 downloads bedragen €{totale_kosten:.2f}")