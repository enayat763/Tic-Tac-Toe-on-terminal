word=[0,1,2,3,4,5,6,7,8,9]

x="X"
z="O"
counter=set()
counta=[]
countb=[]
print(word[1], "**", word[2], "**" ,word[3])
print(word[4], "**" ,word[5], "**" ,word[6])
print(word[5], "**" ,word[8], "**" ,word[9])
def cal(aa,user):
    if user=="player1":
        word[aa]=x
    elif user=="player2":
        word[aa]=z
    print(word[1], "**", word[2], "**" ,word[3])
    print(word[4], "**" ,word[5], "**" ,word[6])
    print(word[7], "**" ,word[8], "**" ,word[9])
az = ('X', 'X', 'X')
ax = ('O', 'O', 'O')
def values():
    value=((word[1], word[2], word[3]),(word[1], word[5], word[9]),(word[1], word[4], word[7]),
    (word[2], word[5], word[8]),(word[3], word[6], word[9]),(word[3], word[5], word[7]),
    (word[4], word[5], word[6]),(word[7], word[8], word[9]),)
    return value

while True:
    storage=values()
    if storage[0] == ax or storage[1]== ax or storage[2]== ax or storage[3]== ax or storage[4]== ax or storage[5]== ax or storage[6]== ax or storage[7]== ax:
            print("player 2 has won")
            break
    while True:
        try:
            b = int(input("player1, choose a socket (1-9): "))
        except:
            print("please enter a number between 1-9")
            continue
        if b>9 or b<1:
            print("please enter a number between 1-9")
            continue
        if b not in counter:
            counter.add(b)
            cal(aa=b, user="player1")
            break
        else:
            print("slot has been taken choose another ")
            continue
    storage=values()
    if storage[0] == az or storage[1]== az or storage[2]== az or storage[3]== az or storage[4]== az or storage[5]== az or storage[6]== az or storage[7]== az:
        print("player 1 has won")
        break
    if len(counter)==9:
        print("No Winner ,Restart the Game")
        break
    while True:
        try:
            c = int(input("player2, choose a socket (1-9): "))
        except:
            print("please enter a number between 1-9")
            continue

        if c>9 or c<0:
            print("please enter a number between 1-9")
            continue
        if c not in counter:
            counter.add(c)
            cal(aa=c, user="player2")
            break
        else:
            print("slot has been taken choose another ")
            continue
    continue


