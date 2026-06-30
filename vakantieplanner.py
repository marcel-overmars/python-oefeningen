# ==========================================================
# PROJECT: VAKANTIEPLANNER
# ==========================================================
#
# In dit project heb ik geoefend met het werken met lijsten.
# Ik heb eerst een lege lijst aangemaakt en daarna bestemmingen
# toegevoegd met append().
#
# Vervolgens heb ik geleerd hoe ik:
# - een bestaand element kan wijzigen;
# - een nieuw element op een specifieke positie kan invoegen
#   met insert();
# - een element uit een lijst kan verwijderen met del;
# - gegevens uit een lijst kan opvragen met zowel positieve
#   als negatieve indexen;
# - string methods zoals .title() kan gebruiken voor een
#   nette weergave;
# - een f-string kan gebruiken om een bericht op te bouwen
#   met gegevens uit de lijst.
#
# Dit project helpt mij om beter te begrijpen hoe lijsten
# tijdens een programma kunnen veranderen, bijvoorbeeld
# wanneer een gebruiker gegevens toevoegt, wijzigt of verwijdert.
# ==========================================================

# ================
# VAKANTIEPLANNER!
# ================


# ============
# Bestemmingen
# ============

print("=============")
print("Bestemmingen")
print("=============")
print()

vakantieplanner = []

vakantieplanner.append('berlijn')
vakantieplanner.append('brussel')
vakantieplanner.append('madrid')
vakantieplanner.append('rome')
vakantieplanner.append('athene')
vakantieplanner.append('kopenhagen')
print(vakantieplanner)
print()

# =======================
# Aanpassingen in planner
# =======================

print("========================")
print("wijzigingen in planning!")
print("========================")
print()

vakantieplanner[-1] = 'amsterdam'
vakantieplanner.insert(1, 'london')
del vakantieplanner[3]
print(vakantieplanner)
print()

# ============================================
# De steden die ik het mooist vind om te zien!
# ============================================

print("===============")
print("Leukere steden!")
print("===============")
print()

print(vakantieplanner[0].title())
print(vakantieplanner[2].title())
print(vakantieplanner[-1].title())
print()

print(f"De steden waar ik meer tijd wil besteden zijn {vakantieplanner[0].title()}, {vakantieplanner[2].title()} en {vakantieplanner[-1].title()}!")


