# A formula based Python program to find sum of series with cubes of first n natural numbers
  
# Returns the sum of series 
def sumOfSeries(n):
    x = (n * (n + 1)  / 2)
    return (int)(x * x)
  
  
   
# Driver Function
n = 5
print(sumOfSeries(n))
  
# Code Contributed by Mohit Gupta_OMG <(0_o)>
