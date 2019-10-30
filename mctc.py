from mctchandler import MCTestCaseHandler
import unittest, sys

class TestMC(MCTestCaseHandler):

    def test_token(self):
        payload = {}
        o = self.server.post('tokentest/',payload)
        print (o)
        #self.assertTrue(True)
    
if __name__ == '__main__':
    unittest.main()
