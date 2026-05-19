"""
Skriv ett program som kan omvandla en temperatur i grader Celsius till grader Fahrenheit.
Version 1, exempel på output:
Skriv in en temperatur i grader Celsius: 22
Det blir 71.6 grader Fahrenheit.
"""

val_f_c = input("Skriv 1 för att räkna om temperaturen till Celsius eller 2 för att räkna om till Fahrenheit: ")

if val_f_c == "1":
    antal_grader_f = float(input("Skriv in en temperatur i grader Fahrenheit: "))
    antal_grader_c = (antal_grader_f - 32) * 5/9
    if antal_grader_c < 10:
        print(f"Det blir {round(antal_grader_c, 1)} Celsius. Ta på dig vinterkläder.")
    elif antal_grader_c >= 20:
        print(f"Det blir {round(antal_grader_c, 1)} Celsius. Packa badkläder!")

elif val_f_c == "2":
    antal_grader_c = float(input("Skriv in en temperatur i grader Celsius: "))
    antal_grader_f = (antal_grader_c * 1.8) + 32
    if antal_grader_f < 50:
        print(f"Det blir {round(antal_grader_f, 1)} Fahrenheit. Ta på dig vinterkläder.")
    elif antal_grader_f >= 68:
        print(f"Det blir {round(antal_grader_f, 1)} Fahrenheit. Packa badkläder!")


else:
    print("Följ instruktionerna och prova igen.")