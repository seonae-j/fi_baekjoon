N = int(input())
a = []


while N%2 == 0:
    a.append(2)
    N = N//2
for i in range(3, 10000000, 2):
    while N%i == 0:
        a.append(i)
        N = N//i
if N>2: 
    a.append(N)

for i in a:
    print(i)