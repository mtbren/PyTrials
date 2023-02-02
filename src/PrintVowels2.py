vowels=['a','e','i','o','u'];
#word='Miiiilliways';
word=input("Enter a word: ");
covered=[];
for c in word:
    if(c in vowels):
        if(c not in covered):
            covered.append(c);
            print(c);