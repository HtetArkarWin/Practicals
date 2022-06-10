from prac_06.guitar import Guitar

guitars=[]

print("My guitars!")
name = str(input("Name: "))
while name!="":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar3 = Guitar(name, year, cost)
    guitars.append(guitar3)
    print(guitars[-1], "added")
    name = str(input("Name: "))

guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

print("These are my guitars:")
for i, guitar in enumerate(guitars):
    vintage_string=" (vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i + 1}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
