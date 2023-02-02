vowelList = ['a','e','i','o','u'];
# vowels = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0};
word = input("Enter any word: ");
# for c in word:
#     if c in vowels.keys():
#         vowels[c] = vowels[c]+1;

# for key in sorted(vowels):
#     print(key,' was found ',vowels[key],' times');
vowels = {};
for c in word:
    if (c in vowelList):
        if(c not in vowels.keys()):
            vowels[c] = 1;
        else:
            vowels[c]+=1;
for k,v in sorted(vowels.items()):
    print(k,' was found ',v,' times');