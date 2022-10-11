with open('in_D_10_Wilczewski.txt', 'r') as f:
    lines = f.readlines()
    A1 = [int(line.rstrip()) for line in lines]
    A2 = A1.copy()
    B1 = []
    B2 = []


 # złożoność pesymistyczną usyskuję gdy żaden element się nie powtarza
 # wtedy będzie wynosić n^2
def D1():
    for i in A1:
        c = A1.count(i)
        B1.append(c * i)
        for j in range(c):
            A1.remove(i)


# sortuje liste metodą sort o złożoności pesymistycznej n*log(n) (Tim sort)
def D2(list):
    list.sort()
    print(list)
    Ans=[]
    count=1
    tmp=list[0]

    for i in range(1,len(list)):
        if list[i] != tmp:
            Ans.append(tmp*count)
            tmp=list[i]
            count=1
        else:
            count+=1
    Ans.append(tmp*count)
    if(rep(Ans)):
        Ans=D2(Ans)
    return Ans
    
    
def rep(list):
    for i in list:
        if(list.count(i)>1):
            return True
    return False        

print(len(D2(A2)))
