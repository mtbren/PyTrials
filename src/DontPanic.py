phrase="Don't panic!";
plist=list(phrase);
print(phrase);
print(plist);

ontap=['o','n',' ','t','a','p'];
for c in plist:
    if c not in ontap:
        plist.remove(c);
print(plist);
plist.pop();
plist.pop();
print(plist);
plist.append(plist.pop(2));
plist.append(plist.pop(4));
plist.append(plist.pop(3));
print(plist);

new_phrase=''.join(plist);
print(new_phrase);
