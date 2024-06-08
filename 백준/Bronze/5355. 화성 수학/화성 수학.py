T = int(input())
for i in range(T) :
    M = list(map(str, input().split()))
    R = float(M[0])
    for i in range(1, len(M)) :
        if M[i] == '@' :
            R *= 3
        if M[i] == '%' :
            R += 5
        if M[i] == '#' :
            R -= 7
    print('{:.2f}'.format(R))