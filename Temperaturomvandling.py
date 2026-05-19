"""
Skriv ett program som kan omvandla en temperatur i grader Celsius till grader Fahrenheit.
Version 1, exempel på output:
Skriv in en temperatur i grader Celsius: 22
Det blir 71.6 grader Fahrenheit.
"""

Antal_grader = float(input("Skriv in en temperatur i grader Celsius: "))
Fahrenheit_grader = (Antal_grader * 1.8) + 32

print(f"Det blir {round(Fahrenheit_grader, 1)} Fahrenheit.")