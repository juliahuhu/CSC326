import math
def rotate(l,n):
 return l[n:] + l[:n]

def rotate_word(s,num):
  x= len(s)
  r=num%x
  t= list(s)
  final_str=''
  final=rotate(t,num-1)
  print  final_str.join(final)
  return final_str.join(final)

rotate_word("hello",3)
