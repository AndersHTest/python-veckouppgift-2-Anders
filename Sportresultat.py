print("Matchen är över, nu ska vi räkna ut resultatet!")

tottenham_goals = int(input("Hur många mål gjorde Tottenham? "))
liverpool_goals = int(input("Hur många mål gjorde Liverpool? "))
tottenham_differens = 0
liverpool_differens = 0

if tottenham_goals > liverpool_goals:
    print(f"Tottenham vann med {tottenham_goals-liverpool_goals} mål!")
elif tottenham_goals < liverpool_goals:
    print(f"Liverpool vann med {liverpool_goals-tottenham_goals} mål!")
else:
    print("Det blev oavgjort.")

"""
Testa med 2-1, 1-2 och 5-5.
"""