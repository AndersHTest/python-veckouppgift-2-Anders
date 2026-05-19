tal1 = int(input("Skriv in det första talet här: "))
tal2 = int(input("Skriv in det andra talet här: "))
tal3 = int(input("Skriv in det tredje talet här: "))

if tal1 >= tal2 and tal1 >= tal3:
    print(f"Det största talet är {tal1}.")
    if tal2 > tal3 and tal2 != tal1 and tal2 != tal3:
        print(f"Det mellersta talet är {tal2}")
    elif tal3 > tal2 and tal3 != tal1 and tal3 != tal2:
        print(f"Det mellersta talet är {tal3}")

elif tal2 >= tal1 and tal2 >= tal3:
    print(f"Det största talet är {tal2}.")
    if tal1 > tal3 and tal1 != tal2 and tal1 != tal3:
        print(f"Det mellersta talet är {tal1}")
    elif tal3 > tal1 and tal3 != tal2 and tal3 != tal1:
        print(f"Det mellersta talet är {tal3}")

else:
    print(f"Det största talet är {tal3}.")
    if tal1 > tal2 and tal1 != tal3 and tal1 != tal2:
        print(f"Det mellersta talet är {tal1}")
    elif tal2 > tal1 and tal2 != tal3 and tal2 != tal1 :
        print(f"Det mellersta talet är {tal2}")

if tal1 == tal2 == tal3:
    print("Alla tal är lika stora.")

if tal1 == tal2 and tal1 != tal3:
    print(f"Två tal är lika stora. Tal 1: {tal1} och Tal 2: {tal2}.")
elif tal1 == tal3 and tal3 != tal2:
    print(f"Två tal är lika stora. Tal 1: {tal1} och Tal 3: {tal3}.")
elif tal2 == tal3 and tal1 != tal3:
    print(f"Två tal är lika stora. Tal 2: {tal2} och Tal 3: {tal3}.")