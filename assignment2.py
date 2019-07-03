
import sys
from webbrowser import get

control = len(sys.argv)
count_arg = control - 1

if count_arg != 3 :
    print("Please run with 3 arguments")
else:
    len1 = len(sys.argv[1])
    len2 = len(sys.argv[2])
    len3 = len(sys.argv[3])
    if len1==len2 or len1==len3 or len2==len3:
        print("Arguments should be a diﬀerent length")
    else:
        alph = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        err1 = 0
        err2 = 0
        err3 = 0
        for i in sys.argv[1]:
            if i not in alph:
                err1+=1
        for i in sys.argv[2]:
            if i not in alph:
                err2+=1
        for i in sys.argv[3]:
            if i not in alph:
                err3+=1
        if err1>0:
            print("Argument",sys.argv[1],"is not a word. All arguments should be word")
        elif err2>0:
            print("Argument",sys.argv[2],"is not a word. All arguments should be word")
        elif err3>0:
            print("Argument",sys.argv[3],"is not a word. All arguments should be word")
        else:
            mylist = []
            for i in sys.argv[1]:
                mylist.append(i)
            for i in sys.argv[2]:
                mylist.append(i)
            for i in sys.argv[3]:
                mylist.append(i)
            mylist.sort()

            print("Find longest word using letters given below")
            say=0
            for j in mylist:
                say+=1
                if say==len(mylist):
                    print("'"+j+"'")
                else:
                    print("'"+j+"',",end="")
            al = str(input("Guess a longest word: "))

            diz = []
            diz.append(sys.argv[1])
            diz.append(sys.argv[2])
            diz.append(sys.argv[3])

            big=""
            normal=""
            small=""

            if al in diz:
                if len(sys.argv[1])>len(sys.argv[2]) and len(sys.argv[1])>len(sys.argv[3]):
                    if len(sys.argv[2])>len(sys.argv[3]):
                        big=sys.argv[1]
                        normal=sys.argv[2]
                        small=sys.argv[3]
                    else:
                        big=sys.argv[1]
                        normal=sys.argv[3]
                        small=sys.argv[2]
                elif len(sys.argv[2])>len(sys.argv[3]) and len(sys.argv[2])>len(sys.argv[1]):
                    if len(sys.argv[1])>len(sys.argv[3]):
                        big=sys.argv[2]
                        normal=sys.argv[1]
                        small=sys.argv[3]
                    else:
                        big=sys.argv[2]
                        normal=sys.argv[3]
                        small=sys.argv[1]
                elif len(sys.argv[3])>len(sys.argv[1]) and len(sys.argv[3])>len(sys.argv[2]):
                    if len(sys.argv[1])>len(sys.argv[2]):
                        big=sys.argv[3]
                        normal=sys.argv[1]
                        small=sys.argv[2]
                    else:
                        big=sys.argv[3]
                        normal=sys.argv[2]
                        small=sys.argv[1]

                if al==big:
                    print("You found a word from list")
                    print("You won 50 points !")
                elif al==normal:
                    print("You found a word from list")
                    print("You won 30 points !")
                else:
                    print("You found a word from list")
                    print("You won 10 points !")

            else:
                print("The word you guessed is not in the list")
                print("You lost !")
