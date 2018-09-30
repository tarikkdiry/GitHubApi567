import unittest
from unittest import mock
# import mock

from hw_04a import gitHubFunction

class TestGitHubFunction(unittest.TestCase):
    # def testValidUserInput1(self):
    #     self.assertEqual(gitHubFunction(1), 'The input username is not valid')

    # def testValidUserInput2(self):
    #     self.assertEqual(gitHubFunction(10), 'The input username is not valid')
    #     self.assertEqual(gitHubFunction(3012), 'The input username is not valid')
    #     self.assertEqual(gitHubFunction([1,2,3]), 'The input username is not valid')
    
    # def testValidUserInput3(self):
    #     self.assertEqual(gitHubFunction("asdasdas"), 'This account does not have any repositories')
    #     self.assertFalse(gitHubFunction("/.123/.123"), 'This account does not have any repositories')

    # def testValidUserInput4(self):
    #     self.assertEqual(gitHubFunction(""), 'You must provide a username')
    #     self.assertEqual(gitHubFunction([]), 'You must provide a username')

    @mock.patch('requests.get')

    def mockGitHubFunction1(self, mockedReq):
        mockedReq.return_value = MockResponse('[{"commits": 1}]')
        result = gitHubFunction(self.user)
        self.assertEqual(len(result), 1)

    def mockGitHubFunction2(self, mockedReq):
        mockedReq.return_value = MockResponse([])
        result = gitHubFunction(self.userInput)
        self.assertEqual(result, "You must provide a username")

    def mockGitHubFunction3(self, mockedReq):
        mockedReq.return_value = MockResponse('[{"commits": 1}, {"commits": 2}]')
        result = gitHubFunction(self.userInput)
        self.assertEqual(len(result), 2)

    def mockGitHubFunction4(self, mockedReq):
        mockedReq.return_value = MockResponse("")
        result = gitHubFunction(self.userInput)
        self.assertEqual(result, "You must provide a username")
    
    def mockGitHubFunction(self, mockedReq):
        mockedReq.return_value = MockResponse(44)
        result = gitHubFunction(self.userInput)
        self.assertEqual(result, "The input username is not valid")
    

if __name__ == '__main__':
    print('Running Unit Tests')
    unittest.main()