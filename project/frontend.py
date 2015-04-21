import numpy
from bottle import *
from backend import *

# This opens up the homepage for our search engine
@route("/")
def page():
	f = open("project.html")
	html = "".join(f.readlines())
	return html

# This helps to open up the homepage for our search engine, which is a static file
@route("/static/<filename>")
def static(filename):
	return static_file(filename, root="html")

# This is the wrapper function that is called when a user click on the search button
@post("/search/")
def handlesearch():
	keyword = request.forms.get("keyword", "")
	line = "/search/%s/1" %(keyword)
	redirect(line)

# This is the actual function that requests a search on the backend and formats the search page
@route("/search//<cpage>")
@route("/search/<keyword>/<cpage>")
def search(keyword="nothing! ", cpage='1'):

	# cpage is the current page of the results that is being displayed
	cpage = int(cpage)
	
	# This is the header for the search results html page
	html1 = """
	<html>
	<head>
		<title> Windrunner - Results </title>
	</head>

	<body bgcolor="#DFFFDF">
	
	"""
	
	# This is the image on the search results html page
	html2 =  """
	
	<div style="position: absolute; align:middle; top:200px; left:750px;">
		<img src="http://images.mmorpg.com/images/newsImages/122012/DOTA2.jpg">
	</div>
	
	"""
	
	# This is the end tags for the search results html page
	html3 = """
	
	</body>
	</html>
	"""
	
	# This is the body for the search results html page when no keyword is entered in the search bar
	inv = """
	</br>
	<font size="30"> Please enter a search keyword!  </font>
	</br>
	"""
	
	# Handles the case where no keyword is entered in the search bar
	if keyword == 'nothing! ':
		return html1 + html2 + inv + html3
	
	# Calculate the theoretical start index and the end index of the results that should be displayed on this page
	tstart = (cpage-1)*10
	tend = (cpage)*10
	
	# Get the list of link titles and link urls from the backend based on this keyword
	lst = backend(keyword)
	links = []
	words = []
	for x,y in lst:
		links.append(x)
		words.append(y)
	
	# Calculate the actual start index and the end index of the results that should be displayed on this page
	# There might be less to be displayed
	if tstart > len(lst):
		start = len(lst)
	else:
		start = tstart
	
	if tend > len(lst):
		end = len(lst)
	else:
		end = tend
	
	# This is the results number
	numbers = range(len(lst)+1)[1:]
	
	kv = [None]*(len(lst)*3)
	if len(lst) > 0:
		kv[::3] = numbers
		kv[1::3] = links
		kv[2::3] = words
		tup = (kv[start*3:end*3])
	else:
		tup = ()
	
	
	# Format the return html line
	# Show the keyword that is entered
	ret1 = """
	</br>
	<p> You are searching for <b> %s </b>. </p>
	</br>
	""" % (keyword)
	
	# Displays 10 search results on a page
	# Show the search results. If there are no other match, the search results will be an empty string
	if end - start > 0:
		results0 = """
		<p> {0}. <a href="{1}">{2}</a> </p>
		"""
	else:
		results0 = ""
	
	if end - start > 1:
		results1 = """
		<p> {3}. <a href="{4}">{5}</a> </p>
		"""
	else:
		results1 = ""
	
	if end - start > 2:
		results2 = """
		<p> {6}. <a href="{7}">{8}</a> </p>
		"""
	else:
		results2 = ""
	
	if end - start > 3:
		results3 = """
		<p> {9}. <a href="{10}">{11}</a> </p>
		"""
	else:
		results3 = ""
	
	if end - start > 4:
		results4 = """
		<p> {12}. <a href="{13}">{14}</a> </p>
		"""
	else:
		results4 = ""
	
	if end - start > 5:
		results5 = """
		<p> {15}. <a href="{16}">{17}</a> </p>
		"""
	else:
		results5 = ""
	
	if end - start > 6:
		results6 = """
		<p> {18}. <a href="{19}">{20}</a> </p>
		"""
	else:
		results6 = ""
	
	if end - start > 7:
		results7 = """
		<p> {21}. <a href="{22}">{23}</a> </p>
		"""
	else:
		results7 = ""
	
	if end - start > 8:
		results8 = """
		<p> {24}. <a href="{25}">{26}</a> </p>
		"""
	else:
		results8 = ""
	
	if end - start > 9:
		results9 = """
		<p> {27}. <a href="{28}">{29}</a> </p>
		"""
	else:
		results9 = ""
	
	results10 = """
	
	</br>
	</br>
	
	"""
	
	# Combines the format strings together
	ret2 = results0 + results1 + results2 + results4 + results4 + results5 + results6 + results7 + results8 + results9 + results10
	
	# Puts the values from the result tuple into the html format string
	ret2 = ret2.format(*tup)
	
	# Displays the page number of the results
	ret3 = '''
	<p> You are in page %s of the results </p> </br>
	''' %(cpage)

	# Displays the link to the previous page and the next page of the search results
	# Previous page link on the first page and next page link on the last page does nothing
	if cpage <= 1:
		ppage = 1
	else:
		ppage = cpage - 1
	
	ret4 = """
		<p> <a href="/search/%s/%s">Previous Page</a> </p>
		
	"""%(keyword, ppage)
	
	if cpage-1 >= len(lst)/10:
		npage = cpage
	else:
		npage = cpage + 1
	
	ret5 = """
		<p> <a href="/search/%s/%s">Next Page</a> </p>
		
	"""%(keyword, npage)
	
	
	# Combines all the return html strings together, forming a html
	ret = html1 + html2 + ret1 + ret2 + ret3 + ret4 + ret5 + html3
	
	# Returns and display everything specified in the html
	return ret



