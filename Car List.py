car = []
carbrand = ""

print ("Enter any car brands you can think of, when finished enter done")
while carbrand != "done":
    carbrand = raw_input("Please enter a brand of car: ")
    if carbrand != "done":
        car.append(carbrand)

for brand in car:
    print brand
print ("\n")
