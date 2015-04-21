#!/usr/bin/env python
#Christian Sangle
#CSC326
#October 15 2012
# Two fuctions that both take strings as input and left Justify's them.
def left_justify(s):
  x=len(s)
  space=50-x
  sl=s+' '*space
  return sl
  
def left_justify_std(s):
  x=len(s)
  space=50-x
  extra_space=0
  sl=s.ljust(space)
  if len(sl)<50:
   extra_space=50-len(sl)
   sl=s.ljust(space+extra_space)
  if len(sl)>50:
   extra_space=len(sl)-50
   sl=s.ljust(space-extra_space)
  return sl
