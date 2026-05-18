print("Matchen är över, nu ska vi räkna ut resultatet!")

tottenham_goals = int(input("Hur många mål gjorde Tottenham? "))
liverpool_goals = int(input("Hur många mål gjorde Liverpool? "))

if tottenham_goals > liverpool_goals:
    print("Tottenham vann!")
elif tottenham_goals < liverpool_goals:
    print("Liverpool vann!")
else:
    print("Det blev lika")