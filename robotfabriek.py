# ==========================================================
# UITLEG PROJECT - ROBOTFABRIEK
# ==========================================================
#
# In dit project oefen ik verder met nesting door meerdere
# dictionaries automatisch aan te maken en deze in één
# lijst op te slaan.
#
# Met een for-loop en range() worden tien robots gemaakt.
# Iedere robot krijgt zijn eigen dictionary, die vervolgens
# met append() aan de lijst wordt toegevoegd. Daarna worden
# de robots vanuit de lijst doorlopen en gecontroleerd.
#
# Gebruikte onderdelen:
# - een lijst met dictionaries
# - dictionaries automatisch aanmaken in een for-loop
# - append() om dictionaries aan een lijst toe te voegen
# - range()
# - for-loops
# - if, elif en else
# - dictionarywaarden ophalen en wijzigen
# - slices
# - len()
# - indexen gebruiken bij een lijst met dictionaries
# - gegevens uit een geneste dictionary ophalen
# - f-strings
#
# Zelf geprogrammeerd als oefening tijdens het leren van
# Python. ChatGPT hielp met de projectopdracht en feedback.
# ==========================================================

# =======================
# 10 robots produceren
# =======================

robots = []

for aantal in range (1, 11):
    robot = {
        'type': 'onderhoudsrobot',
        'energie': 100,
        'snelheid': 'langzaam',
        'status': 'beschikbaar'
    }
    robots.append(robot)

print(robots)
print()

# ===================
# Eerste 5 robots
# ===================

for bot in robots[:5]:
    print(bot)
print()

# ==========================
# Alle robots controleren
# ==========================

for robot in robots:
    if robot['energie'] < 30:
        robot['status'] = 'opladen'
    elif robot['energie'] < 60:
        robot['status'] = 'lage energie'
    else:
        robot['status'] = 'beschikbaar'

for robot in robots:
    print(robot)

# ====================
# Productierapport
# ====================

print("================================")
print("=== ROBOTFABRIEK EINDRAPPORT ===")
print("================================")
print()
print(f"Aantal geproduceerde robots: {len(robots)}")
print(f"Aantal gecontroleerde robots: {len(robots)}")
print(f"Status eerste robot: {robots[0]['status']}")
print(f"Energie laatste robot: {robots[-1]['energie']}")