from datetime import datetime;
import time;
import random;

odd = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,
       31,33,35,37,39,41,43,45,47,49,51,53,55,57,59];


for i in range(1,5):
    print(i);
    min_right_now = datetime.today().minute;
    print(min_right_now);
    if(min_right_now in odd):
        print("Odd!!");
    else:
        print("Even");
    time.sleep(random.randint(1,10));
    
