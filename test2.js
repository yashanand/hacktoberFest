import sympy

def to_find(x):
        find =2
        while(find):
                if(sympy.isprime(x)):
                        #print(x)
                        y = sum(map(int, str(x)))
                        #print(y)
                        if(sympy.isprime(y)):
                                find = find -1
                                print(x)
                x = x+1

x = 1000000
to_find(x)

print(x)
