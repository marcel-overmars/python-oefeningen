# ============================================================
# PROJECT: BIOSCOOP ZAALBEHEER
# ============================================================
#
# In dit project maak ik een eenvoudig beheersysteem voor een
# bioscoop. Het programma laat het verschil zien tussen een
# tuple en een lijst. De filmzalen worden opgeslagen in een
# tuple, omdat deze tijdens het programma niet veranderen.
# De films van vandaag worden opgeslagen in een lijst, omdat
# deze wel gewijzigd kunnen worden.
#
# In dit project oefen ik met:
# - Tuples maken met ()
# - Een tuple uitlezen met indexen
# - Door een tuple lopen met een for-loop
# - len() gebruiken bij een tuple
# - Het verschil tussen tuples en lijsten
# - Lijsten aanpassen met append(), insert(), remove()
#   en indexen
# - Gegevens overzichtelijk weergeven met f-strings
# - Overzichtelijke programma's maken met
#   commentaarblokken
#
# Doel:
# Met dit project leer ik wanneer ik een tuple gebruik en
# wanneer een lijst de betere keuze is. Ik ontdek dat een
# tuple bedoeld is voor gegevens die tijdens het programma
# niet mogen veranderen, terwijl een lijst juist geschikt is
# voor gegevens die regelmatig worden aangepast.
#
# Tijdens het bouwen heb ik geleerd:
# - Dat een tuple wordt gemaakt met ronde haakjes ().
# - Dat de waarden in een tuple door komma's van elkaar
#   worden gescheiden.
# - Dat ik een tuple kan uitlezen met indexen, for-loops en
#   len(), net zoals bij een lijst.
# - Dat ik een tuple niet kan wijzigen met append(),
#   remove(), insert() of door een waarde via een index te
#   vervangen.
# ============================================================

# ===================
# Vaste gegevens
# ===================

filmzalen =(
    'zaal 1',
    'zaal 2',
    'zaal 3',
    'zaal 4',
    'zaal 5',
    'IMAX',
    'VIP',
    '3D',
)

for zaal in filmzalen:
    print(zaal)
print()

print(f"De eerste filmzaal is: {(filmzalen[0])}")
print(f"De laatste filmzaal is: {(filmzalen[-1])}")
print(f"Het aantal zalen is: {len(filmzalen)}")
print()

# ============================
# Films die vandaag draaien
# ============================

films =[
    'avengers',
    'troy',
    'gladiator',
    'spiderman',
    'fast and furious',
]

films.append('venom')
films.append('meg')
films.append('iron man')
films[1] = 'star wars'
films.remove('spiderman')
films.insert(-1, 'the witcher')

# =====================
# Bioscoop overzicht
# =====================

print("=========================")
print("Bioscoop overzicht")
print("=========================")
print()

print(f"Aantal zalen: {len(filmzalen)}")
print(f"Aantal films: {len(films)}")
print()
print("Vaste zalen:")
for zaal in filmzalen:
    print(zaal)
print()
print("Films van vandaag:")
for film in films:
    print(film.title())
print()
print("=========================")