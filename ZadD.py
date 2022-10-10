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
    Ans=[]
    rec=False
    count=0
    list.sort()
    tmp=list[0]
    for i in range(len(list)):
        if list[i] != tmp:
            Ans.append(tmp*count)
            tmp=list[i]
            count=0
        count+=1
        if(count>1):
            rec=True
    Ans.append(tmp*count)
    if rec==True:

        D2(Ans)
    return Ans
D1()
A2=D2(A2)
print(A2)
