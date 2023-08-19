import unittest
from app import app

class TestLoginRoute(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_login_route_returns_200(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_login_route_content(self):
        response = self.app.get('/login')
        self.assertIn(b"Login page", response.data)

if __name__ == '__main__':
    unittest.main()

