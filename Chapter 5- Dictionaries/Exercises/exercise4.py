rivers= {
    "Indus River" : "Pakistan",
    "Ganges River" : "India",
    "Brahmaputra River" : "Bangladesh",
    "Rio Grande de Mindanao River" : "Philippines",
    "Wadi Tayyibah" : "United Arab Emirates",
    }
for river, country in rivers.items():
    print(f"The {river.title()} flow through {country.title()}.")
print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print(f"- {country.title()}")

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print(f"- {river.title()}")