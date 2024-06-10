import statistics

A, B, C = list(map(int, input().split()))
T = A, B, C
second = statistics.median(T)

print(second)