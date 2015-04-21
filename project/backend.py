# Software created by Christian Sangle and Yu Gu Thien
#
# Version: 1.0.0
#
# Function: Takes a word that was passed to it by the front end and 
# searches for it in the datbase of words and returns a list of tuples that
# contain its url and title of the page.
#


def backend(word):
  f=open('dbwords.txt','r')
  isFound=False
  dic={}
  urls=[]
  final_lst=[]
  empty_list=[]
  temp_list=[]
  temp_list2=[]
  ctr=0
  for line in f:
    temp_list.append(line)
  for x in temp_list:
   temp_list2.append(x.split(",",1))
  for x,y in temp_list2:
    if word == x:
       my_list=y
       isFound=True
       break
    else:
       isFound=False
  if isFound==False:
     f.close()
     return final_lst
  else:
     list1=eval(my_list)
     #print my_list
     sorted_list=sort_links(list1)
     doc_ids=[x[0] for x in sorted_list]
     #print len(doc_ids)
     urls=get_urls(doc_ids)
     titles=get_titles(doc_ids)
     #print "len of titles ",len(titles)
     #print "len of URLS",len(urls)
     #print urls
     for x,y in urls:
        ctr=0
        #print x
        for i,j in titles:
            ctr+=1
            if x==i:
              final_lst.append((y,j))
              break
            elif x!=i and ctr==len(titles):
              final_lst.append((y,y))
            else :
              pass
     #print len(final_lst)
     #print final_lst
     return final_lst
     

def sort_links(links):
   """ Takes the sorted link ids and creates a list with of the links 
       where the word is found """

   temp_dict={}
   temp_list=[]
   sorted_list=[]
   ctr=0
   # Open the file where the results is saved and copy the tuple values into an empty list
   h=open('prresults.txt','r')
   for line in h:
    temp_list.append(line)
   #find the comma seperator between the key and the value, and
   #split them, in order to put in dic
   for x in temp_list:
    index=x.find(',')
    key=int(x[0:index])
    val=float(x[index+1:len(x)])
    for y in links:
       if y!= key and ctr==len(links):
          pass
       if y==key:
          temp_dict[key]=val
          break
   #Take dictionary, put it into a list of tuples, 
   #then sort based on the pagerank value, rather then key
   sorted_list= temp_dict.items()
   sorted_list.sort(key=lambda x: x[1],reverse=True)
   
   h.close()
   return sorted_list



def get_urls(links):
    """ Takes the link ids where the word is found and sort them based on 
       their pagerank, and return the resulting list """

    temp_list=[]
    url_list=[]
    temp_list2=[]
   #Open the file where the url's are saved and copy the tuple values into an empty list
    z=open('dbdocs.txt','r')
    for line in z:
      temp_list.append(line)
    #print temp_list
    for x in temp_list:
     index=x.find(',')
     if index==-1:
       y=x.split(" ",1)
       key=int(y[0])
       val=str(x[1]).replace('\n','')
       url_list.append((key,val))
     else:
       #find the tab seperator between the key and the url, and
       #split them, in order to put in a list
       key=x[0:index-1]
       #print key
       value=str(x[index+3:len(x)-1])
       #print value
       temp_list2.append((int(key),value))
    #Find the url's of the links where the word was found
    for k in links:
      for i,j in temp_list2:
       #print j
       if i==k:
        url_list.append((i,j))
        break
    #print len(url_list)
    #print len(links)
    z.close()
    return url_list


def get_titles(links):
    """ Takes the sorted link ids where the word is found and get their 
       titles for the links, and return the resulting list """

    temp_list=[]
    titles_list=[]
    temp_list2=[]
    temp_list3=[]
   # Open the file where the titles's are saved and copy the tuple values into an empty list
    z=open('title.txt','r')
    for line in z:
      temp_list.append(line)
    #find the comma seperator between the key and the value, and
    #split them, in order to put in a list
    for x in temp_list:
      index1=x.find(",")

      if index1==-1:
         pass

      else:
        key=x[:index1]
        val=x[index1:len(x)-1]
        if ',' in key:
          key=key[2:len(x)-1]
        val=x[index1+2:len(x)-2]
        temp_list2.append((int(key),val))
    #print len(links)
    for x in links:
       for i,j in temp_list2:
         if i==x:
           titles_list.append((x,j))
    z.close()
    #print len(links)
    #print len(titles_list)
    return titles_list

#print backend("all")
