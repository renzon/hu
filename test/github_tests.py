from unittest.case import TestCase
from unittest.mock import Mock

from huaula import github

GET_MOCK_RESULT = '''{
  "login": "renzon",
  "id": 3457115,
  "avatar_url": "https://avatars.githubusercontent.com/u/3457115?v=3",
  "gravatar_id": "",
  "url": "https://api.github.com/users/renzon",
  "html_url": "https://github.com/renzon",
  "followers_url": "https://api.github.com/users/renzon/followers",
  "following_url": "https://api.github.com/users/renzon/following{/other_user}",
  "gists_url": "https://api.github.com/users/renzon/gists{/gist_id}",
  "starred_url": "https://api.github.com/users/renzon/starred{/owner}{/repo}",
  "subscriptions_url": "https://api.github.com/users/renzon/subscriptions",
  "organizations_url": "https://api.github.com/users/renzon/orgs",
  "repos_url": "https://api.github.com/users/renzon/repos",
  "events_url": "https://api.github.com/users/renzon/events{/privacy}",
  "received_events_url": "https://api.github.com/users/renzon/received_events",
  "type": "User",
  "site_admin": false,
  "name": "Renzo Nuccitelli",
  "company": "Python Pro",
  "blog": "https://adm.python.pro.br",
  "location": "Brazil",
  "email": "renzo@python.pro.br",
  "hireable": true,
  "bio": null,
  "public_repos": 81,
  "public_gists": 21,
  "followers": 275,
  "following": 3,
  "created_at": "2013-02-02T14:15:53Z",
  "updated_at": "2016-05-01T12:03:33Z"
}'''


class AvatarviTests(TestCase):
    def setUp(self):
        self.get_real = github.requests.get

    def tearDown(self):
        github.requests.get = self.get_real

    def test_avatar_url(self):
        # Esse é um teste unitário, não pode depender de rede ou da lib requests
        response = Mock()
        response.text = GET_MOCK_RESULT
        get_mock = Mock(return_value=response)
        github.requests.get = get_mock
        self.assertEqual('https://avatars.githubusercontent.com/u/3457115?v=3', github.buscar_avatar('renzon'))
        get_mock.assert_called_once_with('https://api.github.com/users/renzon')


class IntegracaoTests(TestCase):
    def test_avatar_url(self):
        self.assertEqual('https://avatars.githubusercontent.com/u/2787697?v=3', github.buscar_avatar('viollarr'))
