a = 0
b = 10
for a in range(a, b): #ou b+1(inferieur mais pas strictement)
    print(a , end='  ')

print('\n')

while(b > 0):
   if b % 2 != 0: 
     print(b, end='  ')    
   b -= 1