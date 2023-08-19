import unittest
from app import app

class TestCreateUser(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_create_user_success(self):
        user_data = {"username": "testuser", "password": "testpassword"}
        response = self.app.post('/create_user', json=user_data)
        data = response.get_json()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(data["message"], "Thông tin người dùng đã được tạo thành công")

    def test_create_user_missing_data(self):
        user_data = {"username": "testuser", "password": "testpassword"}
        response = self.app.post('/create_user', json=user_data)
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["message"], "Dữ liệu không hợp lệ")

if __name__ == '__main__':
    unittest.main()
