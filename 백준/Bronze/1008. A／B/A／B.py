A, B = map(int, input().split())
real = A/B

if (A/B - real) < 10**(-9) or ((A/B - real)/(A/B)) < 10**(-9) : print (real)