vowels = ['a','e','i','o','u'];
alreadyDisplayed = [];
#word = "Milliways";
word = input("Provide a word to search for vowels: ");
for c in word:
    if (c in vowels):
        if (c not in alreadyDisplayed):
            print(c);
            alreadyDisplayed.append(c);
            