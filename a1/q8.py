#Christian Sangle
#CSC326
#October 15 2012
# Takes a list input, and searches through each one determing if any of them are rotated pairs.
import math
def rotate(l, y):
   if len(l) == 0:
      return l
   y = -y % len(l)
   return l[y:] + l[:y]

def rotate_word(s):
  x= len(s)
  n=0
  m=0
  final_str=""
  ctr=0
  while n<x:
   t=list(s[n])
   y=len(t)
   final_str=''
   while ctr<y:
    final=rotate(t,ctr)
    final_str.join(final)
    ctr+=1
    m=0
    while m<x:
	  if m!=n:
	   if final_str.join(final) == s[m]:
	    print (s[m],s[m]),
	  m+=1
   n+=1
