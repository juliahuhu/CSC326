import unittest
from backend import *
from crawler import *
class makeDB (unittest.TestCase):
    #Test if it can make a database
    def test_urllistDoesNotExist (self):
        self.bot=crawler(None, "bad.txt ")
        self.bot.crawl(depth=1)
        self.assertFalse ((self.bot) ==-1, 'this text file exists!')

    def test_emptyUrlList (self):
        self.bot=crawler(None, "empty.txt ")
        self.bot.crawl(depth=1)
        self.assertFalse ((self.bot) ==-1, 'this text file exists!')

    #def test_CreateDataBase (self):
    #    self.bot=crawler(None, "singleurl.txt")
    #    self.bot.crawl(depth=1)

if __name__ == '__main__':
        suite= unittest.TestSuite()
        suite.addTest(unittest.makeSuite(makeDB))
	unittest.TextTestRunner(verbosity=2).run(suite)
        #unittest.main()
