import unittest

from getgitinfo import fetchRepos

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestGithubAPI(unittest.TestCase):
    def testGithub(self):
        self.assertEqual(fetchRepos('?'), "Repository name doesn't exist")
        print('mocking')
    def testGithub2(self):
        expected = ['Repo: CS546_C_Group12_Final_Project  Number of [213 chars]: 6']
        self.assertEqual(fetchRepos('yash171298'), ['Repo: CS-541-Artificial-Intelligence  Number of commits: 23', 'Repo: CS-546-Web-Programming  Number of commits: 12', 'Repo: CS-550  Number of commits: 1', 'Repo: CS-554  Number of commits: 30', 'Repo: CS-554-Web-Programming  Number of commits: 1', 'Repo: CS-562-DBMS2-Project  Number of commits: 2', 'Repo: CS-570-Data-Structures  Number of commits: 1', 'Repo: cs546b_group22_final_project  Number of commits: 30', 'Repo: CS555_A_Project_SpiritualBliss  Number of commits: 30', 
'Repo: CSS-554-WebProgramming-II  Number of commits: 1', 'Repo: CS_554_Group_Project_The_mutables  Number of commits: 30'])
       
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()