import json

seed = input("Enter your seed hash number: ")
f = open(seed + '.json')

data = json.load(f)

possible = True

impossible = []

if data['locations']["Jabu Jabus Belly Barinade Heart Container"] == "Boomerang" or data['locations']["Barinade"] == "Boomerang":
    possible = False
    impossible.append("One of the Barinade rewards is Boomerang")

if data['locations']["Jabu Jabus Belly Map Chest"] == "Boomerang":
    possible = False
    impossible.append("Jabu Jabu Map Chest is Boomerang")
    
if data['locations']["Fire Temple Volvagia Heart Container"] == "Megaton Hammer" or data['locations']["Volvagia"] == "Megaton Hammer":
    possible = False
    impossible.append("One of the Volvagia rewards is Megaton Hammer")

if data['locations']["Spirit Temple Twinrova Heart Container"] == "Mirror Shield" or data['locations']["Twinrova"] == "Mirror Shield":
    possible = False
    impossible.append("One of the Twinrova rewards is Mirror Shield")

if possible:
    print("Your seed is beatable.")
else:
    for impossibility in impossible:
        print(impossibility)

    print("Consider another seed or try your luck to see if the seed is possible regardless\n")

input("Press anything to close")
