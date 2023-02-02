myMap = {
    'Name': 'Amit B',
    'Gender': 'Male',
    'Height': '5.9',
    'Weight': 156
};

print(myMap['Name']);
myMap['Age'] = 33;
print(myMap);

myList = ['Amit', 'Male', '5.9', 156];
print(myList[3]);

word = input("Enter any word: ");
# vMap = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0};
vMap = {};
for c in word:
    if c in ['a', 'e', 'i', 'o', 'u']:
        vMap.setdefault(c,0);
        vMap[c] += 1;

for k, v in sorted(vMap.items()):
    print(k, ' appeared ', v, ' time(s)!');
