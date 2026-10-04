shop = []

while True:
    name_commodity = input("Enter a name_commodity: ")

    if name_commodity == "-1":
        print("Receive Commodity Stop")
        break

    shop.append(name_commodity)

print(shop)
