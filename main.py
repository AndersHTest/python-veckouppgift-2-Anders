"""
Vad är syftet med koden?
Testkör koden med några olika värden.
Finns det några direkta fel i koden? (fel som gör att programmet kraschar)
Finns det logiska fel? (programmet gör något annat än det är tänkt)
Diskutera möjliga lösningar på felen ni hittat.
Diskutera möjliga förbättringar på koden.
"""

level1 = 100
level2 = 300
discount = 0

price = input("Välkommen, ange vad din produkt kostar: ")
price = float(price)

if price > level1 and price <= level2:
    print("Grattis! Du har avancerat till nivå 1 och får 10% rabatt.")
    discount = discount + 10
elif price >= level2:
    print("Grattis! Du har avancerat till nivå 2 och får 25% rabatt.")
    discount = discount + 25

final_price = price * (100 - discount) / 100
print("Efter rabatter blir priset.... " + str(final_price))


"""
1. Syftet med koden verkar vara att 'spelifiera' en butik. Ju mer man spenderar desto mer levlar man upp och desto mer rabatt får man.
2. .. Done
3. Error - Kan inte kombinera final price (float) med string. -Gör om variabeln till string.
4. Man verkar få rabatt både för level 1 och level 2 kombinerat. Det är nog inte avsikten.
5. Man kan göra om if-satserna så att dom hänger ihop istället.
6. is_member-variabeln verkar inte användas så den tar jag bort. Ändra 'köp något dyrt' till något annat. Gör om if-satserna. -> done.
"""
