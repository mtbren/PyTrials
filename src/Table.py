import pprint;

person1 = {'name': 'John', 'age': 37, 'occupation': 'engineer'};
person2 = {'name': 'Meena', 'age': 32, 'occupation': 'engineer'};
people = {'person1': person1, 'person2': person2};

pprint.pprint(people);
pprint.pprint(people['person2']['name']);

mySet = {'a', 'b', 'c', 'a', 'a'};
print(mySet);
