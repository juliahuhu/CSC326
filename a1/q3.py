#Christian Sangle
#CSC326
#October 15 2012
import math
def P(i,j):
# When both are integers compares them and if they are the same integer return 2
# Otherwise,most other cases return 0
#For floating point similar to integers, however, if the float is less then 1
# it will return 0 automatically without looking at the ceiling and floor functions of the two floats
# divided by each other
 if i<=1:
  return 0

 if j<=1:
  return 0
  
 if i<j:
  return P(j,i)
  
 if math.floor(j/i)==math.ceil(i/j):
  return P(i,j-1)+2
  
 else:
  return P(i,j-1)

print P(1.5,3.0)
