# Python3 Program to find sum of square of first n natural numbers
  
  
# Return the sum of
# square of first n
# natural numbers
def squaresum(n) :
  
    # Iterate i from 1 
    # and n finding 
    # square of i and
    # add to sum.
    return sum(x*x for x in range(n,0,-1))
  
# Driven Program
n = 4
print(squaresum(n))
