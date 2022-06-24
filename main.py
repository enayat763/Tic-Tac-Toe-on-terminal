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
    for y in range(1,10):
        if user=="player1":
            if y==aa:
                word[y]=x
        elif user=="player2":
            if y==aa:
                word[y]=z
    print(word[1], "**", word[2], "**" ,word[3])
    print(word[4], "**" ,word[5], "**" ,word[6])
    print(word[7], "**" ,word[8], "**" ,word[9])
az = ('X', 'X', 'X')
ax = ('O', 'O', 'O')
while True:
    ab = (word[1], word[2], word[3])
    ac = (word[1], word[5], word[9])
    ad = (word[1], word[4], word[7])
    ae = (word[2], word[5], word[8])
    af = (word[3], word[6], word[9])
    ag = (word[3], word[5], word[7])
    ah = (word[4], word[5], word[6])
    ai = (word[7], word[8], word[9])

    if ab == ax or ac== ax or ad== ax or ae== ax or af== ax or ag== ax or ah== ax or ai== ax:
            print("player 2 has won")
            break
    while True:
        b = int(input("player1, choose a socket (1-9): "))
        if b>9 or b<1:
            print("please enter a number between 1-9")
            continue
        if b not in counter:
            counter.add(b)
            counta.append(b)
            cal(aa=b, user="player1")
            break
        else:
            print("slot has been taken choose another ")
            continue
    ab = (word[1], word[2], word[3])
    ac = (word[1], word[5], word[9])
    ad = (word[1], word[4], word[7])
    ae = (word[2], word[5], word[8])
    af = (word[3], word[6], word[9])
    ag = (word[3], word[5], word[7])
    ah = (word[4], word[5], word[6])
    ai = (word[7], word[8], word[9])
    if ab == az or ac==az or ad==az or ae==az or af==az or ag==az or ah==az or ai==az:
        print("player 1 has won")
        break
    if len(counta)==5:
        print("No Winner ,Restart the Game")
        break
    while True:
        c = int(input("player2, choose a socket (1-9): "))
        if c>9 or c<0:
            print("please enter a number between 1-9")
            continue
        if c not in counter:
            counter.add(c)
            countb.append(c)
            cal(aa=c, user="player2")
            break
        else:
            print("slot has been taken choose another ")
            continue
    if len(countb)==4:
        print("Restart the Game")    
        break

    continue


