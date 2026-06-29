# ============================================================
# PROJECT: Streaming Abonnement
#
# In dit oefenproject bereken ik de kosten van een streamingdienst
# voor één jaar. De eerste vier maanden krijgen korting en daarna
# wordt het totaalbedrag voor het jaar berekend.
#
# In dit project oefen ik met:
# - Variabelen
# - Lists gebruiken voor de maanden
# - Items uit een list ophalen met indexen
# - String-methodes zoals .title()
# - Rekenen met floats
# - Vermenigvuldigen en aftrekken
# - Berekeningen opslaan in nieuwe variabelen
# - F-strings gebruiken
# - print() gebruiken voor nette uitvoer
# - \t gebruiken om tekst uit te lijnen
# - Het programma indelen met duidelijke kopjes en commentaar
#
# Doel:
# Een overzichtelijk programma maken dat laat zien wat een
# jaarabonnement kost, hoeveel korting er wordt gegeven en wat
# het eindbedrag is.
# ============================================================


# Actuele prijs streamingsdienst!

print("=-=-=-=-=-=-=-=")
print("Actuele prijs")
print("=-=-=-=-=-=-=-=")
print()

maand = ['januari', 'februari', 'maart', 'april', 'mei', 'juni', 'juli', 'augustus', 'september', 'oktober', 'november', 'december']
prijs = 12.99
aantal_maanden = 12
totaal_prijs = prijs * aantal_maanden
print(f"De actuele prijs voor de streamingsdienst is {totaal_prijs} per 12 maanden!")
print()

# Korting streamingsdienst

print("=========")
print("KORTING")
print("=========")
print()
print(f"De maanden {maand[0].title()}, {maand[1].title()}, {maand[2].title()}, {maand[3].title()} krijgt u 50% korting!!! ")
print(f"Dat is dus de eerste 4 maanden korting!")

korting = 0.50
totaal_korting = (prijs * 4) * korting
print(f"Over 4 maanden is dat €{totaal_korting} korting!")
print()

# Totaal voor jaar abbonement!

maand_korting = prijs * korting

print("===============")
print("TOTAAL BEDRAG")
print("===============")
print()
print(f"{maand[0].title()}\t\t{maand_korting}")
print(f"{maand[1].title()}\t{maand_korting}")
print(f"{maand[2].title()}\t\t{maand_korting}")
print(f"{maand[3].title()}\t\t{maand_korting}")
print(f"{maand[4].title()}\t\t{prijs}")
print(f"{maand[5].title()}\t\t{prijs}")
print(f"{maand[6].title()}\t\t{prijs}")
print(f"{maand[7].title()}\t{prijs}")
print(f"{maand[8].title()}\t{prijs}")
print(f"{maand[9].title()}\t\t{prijs}")
print(f"{maand[10].title()}\t{prijs}")
print(f"{maand[11].title()}\t{prijs}")
print()

eind_bedrag = totaal_prijs - totaal_korting
print(f"Voor een jaarabonnement betaal je dus in totaal €{eind_bedrag}!")
