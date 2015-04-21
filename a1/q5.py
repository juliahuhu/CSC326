#Christian Sangle
#CSC326
#October 15 2012
#Rotates a word inputted by the user by the integer specified by the user counter clockwise.
import math
def rotate(l, y):
   if len(l) == 0:
      return l
   y = -y % len(l)           #Rotates the letter counter clockwise
   return l[y:] + l[:y] 

def rotate_word(s,num):
  x= len(s)
  if s =='':                 #Enter a blank space si valid
   return ""
  if x<=0:                   #Entering a void, null or illegal word will result in failure.
   return False
  else:
    r=num%x                 #Get the remainder between the length of the word and the rotation nubmer specified by user.
    t= list(s)              # Turn string into a list of characters, so it is unmutable and can be worked with.
    final_str=''
    final=rotate(t,r)
  return final_str.join(final)  #Turn list back into a string and return.
