# ==========================================================
# UITLEG PROJECT - ROBOT FACTORY
# ==========================================================
#
# In dit project maak ik een registratiesysteem voor een
# robotfabriek. Robots worden geregistreerd, geproduceerd
# en bijgewerkt. Daarna wordt een eindrapport gemaakt.
#
# Gebruikte onderdelen:
# - Functies met def en return
# - Een dictionary teruggeven vanuit een functie
# - Optionele parameters met None
# - Meerdere dictionaries maken met range()
# - Dictionaries opslaan in een lijst met append()
# - Slicing om een gedeelte van de lijst te selecteren
# - Dictionarywaarden aanpassen met for en if
# - Robots tellen met for, if en += 1
#
# Het belangrijkste oefenonderdeel was het teruggeven
# van een dictionary met return en het herhalen van
# oudere technieken uit hoofdstuk 6.
#
# Zelf geprogrammeerd als oefening tijdens het leren
# van Python. ChatGPT hielp met de opdracht en feedback.
# ==========================================================

# ======================
# Robot registreren
# ======================

def maak_robot(
        naam,
        type_robot,
        energie,
        specialisatie=None
):
    robot = {
        'naam': naam,
        'type': type_robot,
        'energie': energie,
    }
    if specialisatie:
        robot['specialisatie'] = specialisatie

    return robot

robot_1 = maak_robot(
    'Atlas',
    'Industrieel',
    100
)

robot_2 = maak_robot(
    'Nova',
    'Onderzoek',
    85,
    'Ruimtevaart'
)

robot_3 = maak_robot(
    'Titan',
    'Beveiliging',
    120
)

print(robot_1)
print(robot_2)
print(robot_3)
print()

# ====================
# Robots produceren
# ====================

fabrieksrobots = []

for robots in range(1, 21):
    robot = {
        'type': 'werkrobot',
        'energie': 100,
        'status': 'stand-by'
    }
    fabrieksrobots.append(robot)

for robots in fabrieksrobots:
    print(robots)
print()

# ========================================
# Een gedeelte van de robots aanpassen
# ========================================

for robots in fabrieksrobots[:5]:
    if robots['type'] == 'werkrobot':
        robots['energie'] = 150
        robots['status'] = 'actief'

for robots in fabrieksrobots:
    print(robots)
print()

# ===============
# Eindrapport
# ===============

print("=====================")
print("=== ROBOT FACTORY ===")
print("=====================")
print()
print("GEREGISTREERDE ROBOTS")
print()
print(robot_1)
print(robot_2)
print(robot_3)
print()
print("PRODUCTIEOVERZICHT")
print()
print(f"Totaal geproduceerde werkrobots: {len(fabrieksrobots)}")

actieve_robots = 0

for robot in fabrieksrobots:
    if robot['status'] == 'actief':
        actieve_robots += 1
print(f"Actieve werkrobots: {actieve_robots}")

inactieve_robots = 0

for robot in fabrieksrobots:
    if robot['status'] == 'stand-by':
        inactieve_robots += 1
print(f"Werkrobots op standby: {inactieve_robots}")