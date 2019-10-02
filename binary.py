# Uses python3
import sys

def binary_search(a, x):
	    first = 0
	    last = len(a)-1
	    found = False
	    f=-1
	    while first<=last and not found:
	        midpoint = (first + last)//2
	        if a[midpoint] == x:
	            found = True
	            f=midpoint
	        else:
	            if x <a[midpoint]:
	                last = midpoint-1
	            else:
	                first = midpoint+1
	
	    return f
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, x), end=" ")
