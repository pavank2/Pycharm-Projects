n = 123
rev = 0

length = len(str(n))
i=length
while i > 0:
    rev += (n%10) * (10**(i-1))
   
    i = i -1
    n = n // 10


print(rev)