import math

T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    for j in range(1):
        print(abs(A*B)//math.gcd(A, B))