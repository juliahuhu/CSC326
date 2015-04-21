import numpy as np
from numpy import*
from functools import wraps

def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print func.__name__ + " was called"
        return func(*args, **kwargs)
    return with_logging

@logged
def f(x):
 y=float(10*(x**2)+3*x+1)
 return y

def integrate(f,a,b,n):
 h=(b-a)/float(n-1)
 final=(h*(f(a)+f(b)))/2.0
 s=0.0
 for i in xrange(1,n-1):
  s+=f(a+i*h)
 final+=s
 return final/float(n-1)

def integrate_fast(f,a,b,n):
 b=linspace(a,b,n)
 vfunc=np.vectorize(f)
 x=vfunc(b)
 c=np.sum(x)
 final=c/(n-1)
 return final

def integrate_speedup(f,a,b,n):
 import timeit
 t1=timeit.timeit("integrate(f,a,b,n)", setup= "from q1 import integrate")
 t2=timeit.timeit("integrate_fast(f,a,b,n)", setup= "from q1 import integrate_fast")
 final_t=t1/float(t2)
 return final_t

integrate_speedup(f,1,2,500)
