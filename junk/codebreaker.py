import random
from turtle import end_fill
code = str(random.randint(1000, 9999))
flag= True
count = 1


def ordinaltg():
    return str(count) + {1: 'st', 2: 'nd', 3: 'rd'}.get(4 if 10 <= count % 100 < 20 else count % 10, "th")


while (flag):
    response = ["_","_","_","_"]
    print ("What is your " + ordinaltg() + " guess?")
    
    answer = str(input())  
    if answer == "end":
        flag = False  
    elif answer == code:
        print ("You did it!")
        flag = False
    else:
        for x in range(len(code)):
            if answer[x] == code[x]:
                response[x] = "1"
            else:
                for i in range(len(code)):
                    if code[i] == answer[x]:
                        response[x] = "0"
        print (*response)
        count += 1
        if count == 5:
            flag = False
            print ("You didn't do it in time! The safe is locked forever now :(")


    



        


