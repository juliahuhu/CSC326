import random
import numpy as np

def estimate_dist(n):
 temp_list=[0]*n
 ctr=0
 for i in xrange(0,n):
  x=random.randint(1,20)
  temp_list[i]=x
 for j in xrange(0,n):
  if temp_list[j] == 10:
   ctr+=1
 if ctr==0:
  val="%0.2f" % 0
 else:
  val= "%0.2f" %((ctr/float(n))*100)
 return val

def count_num(a):
 if a==10:
  return 1
 else:
  return 0

def estimate_dist_fast(n):
 b=np.random.randint(1,21,size=n)
 vfunc=np.vectorize(count_num)
 a=vfunc(b)
 x=np.sum(a)
 if x==0:
  val="%0.2f" % 0
 else:
  val= "%0.2f" %((x/float(n))*100)
 return val

print estimate_dist_fast(23)
print estimate_dist(23)


