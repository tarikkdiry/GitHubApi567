import unittest
from hw_04a import gitHubFunction
from unittest import mock
from unittest.mock import MagicMock

class TestGitHubFunction(unittest.TestCase):
    @mock.patch('hw_04a.gitHubFunction')
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