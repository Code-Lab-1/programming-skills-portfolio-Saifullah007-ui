pets = []

pet = {
    "Animal Type": "Abyssinian Cat",
    "Owner": "abood",
}
pets.append(pet)

pet = {
    "Animal Type": "American Bobtail Cat",
    "Owner": "rashood",
}
pets.append(pet)
pet = {
    "Animal Type": "Bengal Cat",
    "Owner": "hasson",
}
pets.append(pet)

pet = {
    "Animal Type": "American Curl Cat",
    "Owner": "alo",
}
pets.append(pet)

for pet in pets:
    print(f"\n Below are the Details about the pet {pet['Animal Type'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")