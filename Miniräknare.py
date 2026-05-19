tal1 = int(input("Skriv in det första talet här: "))
tal2 = int(input("Skriv in det andra talet här: "))
tal3 = int(input("Skriv in det tredje talet här: "))

if tal1 > tal2 and tal1 > tal3:
    print(f"{tal1} är det största talet.")
elif tal2 > tal1 and tal2 > tal3:
    print(f"{tal2} är det största talet.")
elif tal3 > tal1 and tal3 > tal2:
    print(f"{tal3} är det största talet.")
else:
    print(f"Kunde inte hitta det största talet. Är talen lika stora?")