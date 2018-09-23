import unittest

from hw_04a import gitHubFunction

class TestGitHubFunction(unittest.TestCase):
    def testValidUserInput1(self):
        self.assertEqual(gitHubFunction(1), 'The input username is not valid')

    # def testValidUserInput2(self):
    #     self.assertEqual(gitHubFunction(10), 'The input username is not valid')

    # def testValidUserInput3(self):
    #     self.assertEqual(gitHubFunction("asdasdas"), 'This account does not have any repositories')

    # def testValidUserInput4(self):
    #     self.assertEqual(gitHubFunction(""), 'You must provide a username')

    # def testValidUserInput5(self):
    #     self.assertTrue(gitHubFunction("tarikkdiry"))

    # def testValidUserInput6(self):
    #     self.assertFalse(gitHubFunction("asdasda"))

if __name__ == '__main__':
    print('Running Unit Tests')
    unittest.main()