def minion_game(string):
    s =0
    k =0
    vovl = ["A","E","I","O","U"]
    for i in range(len(string)):
        if string[i] in vovl:
            k += len(string)-i
        else:
            s += len(string)-i
    if s>k:
        print("Stuart {}".format(s))
    elif(s==k):
        print("Draw")
    else:
        print("Kevin {}".format(k))
        

if __name__ == '__main__':
    s = input()
    minion_game(s)
