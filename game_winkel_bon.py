item_1 = "zwaard"
item_2 = "schild"
item_3 = "health potion"

prijs_1, prijs_2, prijs_3 = 49.99, 35.50, 4.99

BTW_PERCENTAGE = 0.21

subtotaal = prijs_1 + prijs_2 + prijs_3
btw = subtotaal * BTW_PERCENTAGE
totaal = subtotaal + btw

print("===================")
print("GAME WINKEL BON")
print("===================")
print()
print(f"\t{item_1.title()}\n\t{item_2.title()}\n\t{item_3.title()}")
print()
print(f"Subtotaal: €{subtotaal}\nBTW: €{btw}\nTotaal: €{totaal}")
print()
print(f"Bedankt voor je aankoop!")