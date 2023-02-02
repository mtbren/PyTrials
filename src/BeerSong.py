word = "bottles";
for i in range(10,0,-1):
    print(i,word,"of beer on the wall");
    print(i,word,"of beer");
    print("Take one down");
    print("Pass it around");

    if(i == 2):
        word = "bottle"

    if(i == 1):
        print("No more bottles of beer on the wall");
    else:    
        print(i-1,word,"of beer on the wall");
        
    print();
