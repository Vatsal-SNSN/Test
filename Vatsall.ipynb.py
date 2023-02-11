#Slightly modified binary search, now searches in 2nd element in a list of tuples
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid][1] == x:
            return arr[mid][0]
        elif arr[mid][1] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Function to check if winner is found
def checker(arr):
    if arr[1]==arr[2] and arr[2]==arr[3]:
        if arr[1]==1:
            return 1
        elif arr[1]==0:
            return 0
    elif arr[4]==arr[5] and arr[5]==arr[6]:
        if arr[4]==1:
            return 1
        elif arr[4]==0:
            return 0
    elif arr[7]==arr[8] and arr[8]==arr[9]:
        
        if arr[7]==1:
            return 1
        elif arr[7]==0:
            return 0
    elif arr[1]==arr[5] and arr[1]==arr[9]:
        if arr[1]==1:
            return 1
        elif arr[1]==0:
            return 0
    elif arr[3]==arr[5] and arr[5]==arr[7]:
        if arr[3]==1:
            return 1
        elif arr[3]==0:
            return 0
    elif arr[1]==arr[4] and arr[4]==arr[7]:
        if arr[1]==1:
            return 1
        elif arr[1]==0:
            return 0
    elif arr[2]==arr[5] and arr[5]==arr[8]:
        if arr[2]==1:
            return 1
        elif arr[2]==0:
            return 0
    elif arr[3]==arr[6] and arr[6]==arr[9]:
        if arr[3]==1:
            return 1
        elif arr[3]==0:
            return 0
    else:
        return -1
    
#Fresh game, empty board and no outcome (emp is list of empty places)
outcome=-1
board={1:-1,2:-1,3:-1,4:-1,5:-1,6:-1,7:-1,8:-1,9:-1}
emp=[1,2,3,4,5,6,7,8,9]
     
#Game loop, while outcome is not reached keep running
     
while outcome==-1 or outcome==None:
    #prints board
    for i in range(1,10):
        if i==4 or i==7:
            print()
        if board[i]==-1:
            print(i,end="")
            print(" | ",end="")
            continue
        if board[i]==0:
            print("O",end="")
            print(" | ",end="")
            continue
        if board[i]==1:
            print("X",end="")
            print(" | ",end="")
            continue
    print()
    print()
    print()
    
    play=int(input("Where to place X"))
    
    #Bad inputs
    if play not in emp:
        print("Illegitimate move! Box already taken")
        continue
    
    if i>9 or i<0:
        print("Illegitimate move! Enter available box number on display.")
        continue
    #For board, -1 ---> Empty, 0---> played by computer (O), 1---> played by user (X)
    
    board[play]=1
    outcome = checker(board)
    
    #Sees if any immediate result is reached
    
    if outcome==0 or outcome==1:
        break
    emp.remove(play)
    if len(emp)==1:
        board[emp[0]]=0
        outcome = checker(board)
        break
    #prints board 
    for i in range(1,10):
        if i==4 or i==7:
            print()
        if board[i]==-1:
            print(i,end="")
            print(" | ",end="")
            continue
        if board[i]==0:
            print("O",end="")
            print(" | ",end="")
            continue
        if board[i]==1:
            print("X",end="")
            print(" | ",end="")
            continue
    print()
    print()
    print()
    
    score={}
    convert=[]
    #Makes the list connecting i to board position (i is connected to score in score dictionary)
    for i in range(len(emp)):
        convert.append((emp[i],i))
    
	#result not found, tries every possible move and assigns them a score
    for i in range(len(emp)):
        score[i]=0
        a=emp.copy()
        tboard=board.copy()
    
        tboard[a[i]]=0
        a.remove(a[i])
    
        toutcome=checker(tboard)
        if toutcome==0:
            score[i]+=100
            continue
        if len(a)==0:
            break

        for j in range(len(emp)-1):
            b=a.copy()
            z=tboard.copy()

            z[b[j]]=1
            b.remove(b[j])

            if checker(z)==1:
                score[i]-=100
                break
            if len(b)==0:
                    break

            for k in range(len(emp)-2):
                c=b.copy()
                y=z.copy()

                y[c[k]]=0
                c.remove(c[k])

                if checker(y)==0:
                    score[i]+=1
                    break
                if len(c)==0:
                    break

                for l in range(len(emp)-3):
                    d=c.copy()
                    x=y.copy()

                    x[d[l]]=1
                    d.remove(d[l])

                    if checker(x)==1:
                        score[i]-=1
                        break
                    if len(d)==0:
                        break


                    for m in range(len(emp)-4):
                        e=d.copy()
                        w=x.copy()

                        w[e[m]]=0
                        e.remove(e[m])

                        if checker(w)==0:
                            score[i]+=1
                            break
                        if len(e)==0:
                            break

                        for n in range(len(emp)-5):
                            f=e.copy()
                            v=w.copy()

                            v[f[n]]=1
                            f.remove(f[n])

                            if checker(v)==1:
                                score[i]-=1
                                break
                            if len(f)==0:
                                break

                            for o in range(len(emp)-6):
                                g=f.copy()
                                u=v.copy()

                                u[g[o]]=0
                                g.remove(g[o])

                                if checker(u)==0:
                                    score[i]+=1
                                    break
                                if len(g)==0:
                                    break

                                u[g[0]]=1
                                if checker(u)==1:
                                    score[i]-=1
                                break
                        
    #best move found, registers it
    pol=list(score.values())
    #if no moves available, check outcome and break
    if pol==[]:
        outcome=checker(board)
        if outcome !=0 and outcome !=1:
            outcome=2
            break
        else:
            break
    #else, find i of best move
    bestscore=max(pol)
    for i,j in score.items():
        if j==bestscore:
            position=i
	#Use binary search to find board position (through i) of best move
    gen=binary_search(convert,position)
    #play best move
    board[gen]=0
    emp.remove(gen)
    print("Computer has moved!")
    print()
    outcome=checker(board)

#outcome = 0 ---> win, 1---> loss
if outcome==0:
    print("Computer wins!")
    for i in range(1,10):
        if i==4 or i==7:
            print()
        if board[i]==-1:
            print(i,end="")
            print(" | ",end="")
            continue
        if board[i]==0:
            print("O",end="")
            print(" | ",end="")
            continue
        if board[i]==1:
            print("X",end="")
            print(" | ",end="")
            continue
            
elif outcome==1:
    print("You win!")
    for i in range(1,10):
        if i==4 or i==7:
            print()
        if board[i]==-1:
            print(i,end="")
            print(" | ",end="")
            continue
        if board[i]==0:
            print("O",end="")
            print(" | ",end="")
            continue
        if board[i]==1:
            print("X",end="")
            print(" | ",end="")
            continue
#since game has ended without win or loss, it is draw
else:
    print("It's a draw!")
    for i in range(1,10):
        if i==4 or i==7:
            print()
        if board[i]==-1:
            print(i,end="")
            print(" | ",end="")
            continue
        if board[i]==0:
            print("O",end="")
            print(" | ",end="")
            continue
        if board[i]==1:
            print("X",end="")
            print(" | ",end="")
            continue
