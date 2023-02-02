list1=[1,2,3];
list2=list1;
print(list1);
print(list2);
list3=list2.copy();
list2.append(4);
print(list1);
print(list2);
print(list3);

print(list2[0]);
print(list3[0]);
print(list2[-1]);
print(list3[-1]);

list4=list('abcdefghijklmnopqqrstuvwxyz');
print(list4[0:9:2]);

