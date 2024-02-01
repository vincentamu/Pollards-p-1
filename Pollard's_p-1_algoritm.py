import math

import sympy

def pollard(n):
    # base
    a = 2

    # exponent
    k = 2


    while(True):
        
        a = (a**k) % n
        #print("a = ",a)

        d = math.gcd((a-1), n) #checks if there is a common denominator break if d > 1.
        #print(d)
        if(d > 1):
            return d
            break

        k += 1
        



num = 340510176929609558738506407941198102081020749940944635553628097992090306553579338501 #Test number change if needed.
#to hold the factors
ans = []

    
d = pollard(num)

ans.append(d)

ans.append(int(num/d))

print(ans)
    
    