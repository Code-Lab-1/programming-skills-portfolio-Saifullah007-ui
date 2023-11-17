while True:
    age=int(input("your age is=="))
    if age=="Leave":
        break
    if age< 3 or age== 3:
        print("mam u get free ticket!")
    elif age< 13 or age== 13:
        print("Mam u will get ticket for 10$")
    else:
        print("Mam u will get ticket for 15$")
        break