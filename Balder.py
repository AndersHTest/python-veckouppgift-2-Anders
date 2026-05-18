"""
För att få åka Balder på Liseberg måste man vara 130 cm lång. Skriv ett program som kan säga om man får åka!
"""

user_length = int(input(f"Fyll i hur lång du är i centimeter: "))

if user_length >= 130:
    print(f"Du får åka!")
else:
    print(f"Du får inte åka!")

"""
* Tre värden används för att testa alla jämförelseoperatörer mer, mindre & är lika med.
* Se föregående svar ^.
* Testvärdet 129 hade varit överflödigt då vi redan har testat 'mindre än'.
"""