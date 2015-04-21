from crawler import *
from frontend import *
from backend import *


#bot = crawler(None, "urllist.txt")
#bot.crawl(depth=1)

run(host="localhost", port=8080, debug=True)
# Open a browser and type in "localhost:8080"
