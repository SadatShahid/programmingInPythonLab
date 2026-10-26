ch = input("Enter a character: ")

if ch.lower() in "aeiou" and len(ch) == 1:
    print("Vowel")
else:
    print("Not vowel")
