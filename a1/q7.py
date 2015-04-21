#Christian Sangle
#CSC326
#October 15 2012
# Looks for similar values in a list, if there is a match return the position of teh first one found
def num_contain(str,list):
 for i in range (len(list)-1):
  if str in list[i]:
   return i
 return
 
