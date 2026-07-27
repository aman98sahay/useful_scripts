



# /usr/bin/python3 /Users/aman/Desktop/RJ/tables.py > tables.txt

table_of =  921

# for i in range (1 , 11) :
#     print(f"{table_of} X {i} = {i*table_of}")   

# exit(0)

circle = ["apple","banana", "cat","dog","ear","Fat","goat","hot","ice-cream","joker", "king"]

verbose = False

for j in range (0,8):

    for i in range (1 , 11) :
        if verbose:
            print(f"{table_of} X {i} = {i*table_of}")   
        else:
            if i != 10:
                print(f" {circle[i-1]} {circle[i]} {i*table_of}")   
            else :
                print(f" {circle[i-1]} {circle[i]} {(i*table_of - 10)// 10}X")   

    print("abcdefghi")
    
    table_of += 10


