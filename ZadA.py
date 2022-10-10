with open('in_A_10_Wilczewski.txt', 'r') as f:
    n = int(f.readline())
    m = int(f.readline())


def Silnia(x):
    print("count")
    if x > 1:
        return x * Silnia(x - 1)
    return 1

# złożoność  równa: n+m+(n-m)=2n

def A1(n, m):
    result = Silnia(n) / (Silnia(m) * Silnia(n - m))
    return int(result)

# złożoność równa

def A2(n, m):
    result = 1
    for i in range(1, m + 1):
        result *= (n - i + 1) / i
    return int(result)


with open('out_A_10_Wilczewski.txt', 'w') as f:
    f.write(str(A1(n,m))+'\n'+str(A2(n,m)))
   # f.write(str(A2(n,m)))

