import json
import unittest
from unittest.mock import patch
from unittest.mock import Mock
import getgitinfo
@patch("getgitinfo.fetchRepos",return_value=['Repo: CS-541-Artificial-Intelligence  Number of commits: 23', 'Repo: CS-546-Web-Programming  Number of commits: 12', 'Repo: CS-550  Number of commits: 1', 'Repo: CS-554  Number of commits: 30', 'Repo: CS-554-Web-Programming  Number of commits: 1', 'Repo: CS-562-DBMS2-Project  Number of commits: 2', 'Repo: CS-570-Data-Structures  Number of commits: 1', 'Repo: cs546b_group22_final_project  Number of commits: 30', 'Repo: CS555_A_Project_SpiritualBliss  Number of commits: 30', 
 'Repo: CSS-554-WebProgramming-II  Number of commits: 1', 'Repo: CS_554_Group_Project_The_mutables  Number of commits: 30'])
class TestHw04a(unittest.TestCase):
    def test_fetch_user_repo_mock_api(self, mock_fetch_user_repo):
        response_file = open('./response_fetch_user_repo.json')        
        repo_call_response = json.load(response_file)
        mock_fetch_user_repo.return_value = Mock(status_code = 200)
        mock_fetch_user_repo.return_value.json = repo_call_response
        response = getgitinfo.fetchRepos('yash171298')
        self.assertEqual(response.json[0]['name'],"chatbot_ner")
        response_file.close()

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()