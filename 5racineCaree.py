import math
num = float(input("Enter the number : "))

if num >= 0 :
    square_root = math.sqrt(num) 
    print("The square root of {0} = {1}".format(num,square_root))
else: print("   ERROR !") 