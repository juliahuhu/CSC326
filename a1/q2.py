#Christian Sangle
#CSC326
#October 15 2012
# Takes input of Rows and Columns and prints an Asci table of that length.
def print_end():
 print
 
def print_post() :
 print '|        ',
 
def print_beam():
 print '+ - - - -',
 
def print_beams(y):
  n=0
  while n<y :
   print_beam()
   n+=1
  print '+'
  
def print_posts(x):
 m=0
 while m<x:
  print_post()
  m+=1
 print'|'

def print_ascirow(x,y):
   print_beams(y)
   ctr=0
   while ctr<=4:
    print_posts(y)
    ctr+=1
 
def print_box(x,y):
 if x<=0:
   print_end()
 else :
  ctr2=0
  while ctr2 <x:
   print_ascirow(x,y)
   ctr2+=1
  print_beams(y)
   
  
   
 
#print_box(0,0)