T = int(input())

for i in range (T) :
    S = list(map(str, input().split()))
    R1 = int(S[0])
    R2 = S[1]
    for j in range(len(R2)) : 
        for k in range(R1) :
            print(R2[j], end="")
    print()