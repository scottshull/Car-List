cars = []
carbrand = ""

print ("Enter any car brands you can think of, when finished enter done")
while carbrand != "done":
    carbrand = raw_input("Please enter a brand of car: ")
    if carbrand != "done":
        cars.append(carbrand)

for car in cars:
    print car
print ("\n")

cars.sort()
for car in cars:
    print car
print ("\n")
