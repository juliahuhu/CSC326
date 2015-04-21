def rotate_word(str,int):
 x= len(str)
 r=int%x
 t= list(str)
 final=list(str)
 final_str=''
 n=0
 m=1
 while n<x:
  if r-m<x:
   final[n]=t[r-m]
  else:
   print n
   y=n+r-x-1
   print y
   final[n]=t[y]
  n+=1
  m-=1
 
 print  final_str.join(final)
 return final_str.join(final)

rotate_word("hello",1)