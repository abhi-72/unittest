import unittest
from config import HOST,USER
from mctreqhandler import MCTestRequestHandler

class MCTestCaseHandler(unittest.TestCase):

    def setUp(self):
        self.server = MCTestRequestHandler(f"http://{HOST}",{'username':USER})
        print('-'*80)
        print("{0:4} {1:50} {2:6} {3}".format(' # ','TEST CASE NAME','RESULT','COMMENTS'))
        print('-'*80)

