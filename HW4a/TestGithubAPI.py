import unittest

from getgitinfo import fetchRepos

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestGithubAPI(unittest.TestCase):
    def testGithub(self):
        self.assertEqual(fetchRepos('?'), "Repository name doesn't exist")
    def testGithub2(self):
        expected = ['Repo: CS546_C_Group12_Final_Project  Number of [213 chars]: 6']
        self.assertEqual(fetchRepos('SeeAnish'), ['Repo: CS546_C_Group12_Final_Project  Number of commits: 30', 'Repo: CS555-Agile-Methods-for-Software-Development  Number of commits: 2', 'Repo: CS_555_C_Atom  Number of commits: 30', 'Repo: SSW567  Number of commits: 20', 'Repo: SSW_567_HW01  Number of commits: 6'])
       
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()