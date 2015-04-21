#Christian Sangle
#CSC326
#October 15 2012
#Function that finds the GCD of two numbers.
def gcd(a,b):
 if b==0 :
  return a
 else:
  return gcd (b,a%b)
