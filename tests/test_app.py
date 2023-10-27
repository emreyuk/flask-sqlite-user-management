import unittest
import json
from app import app

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_user(self):
        response = self.app.get('/users/1')
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['id'], 1)

    def test_get_user_not_found(self):
        response = self.app.get('/users/1000')
        self.assertEqual(response.status_code, 404)

    def test_delete_user(self):
        response = self.app.delete('/users/1')
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Kullanıcı ID 1 başarıyla silindi')

    def test_delete_user_not_found(self):
        response = self.app.delete('/users/1000')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['message'], 'Kullanıcı bulunamadı')

    def test_get_users_all(self):
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertTrue(isinstance(data, list))

    def test_create_user(self):
        new_user = {
            'id': 3,
            'username': 'newuser',
            'email': 'newuser@example.com'
        }
        response = self.app.post('/users', json=new_user)
        self.assertEqual(response.status_code, 201)

    def test_create_user_invalid_data(self):
        invalid_user = {
            'id': 4,
            'username': 'newuser'
        }
        response = self.app.post('/users', json=invalid_user)
        self.assertEqual(response.status_code, 400)

    def test_update_user(self):
        updated_user = {
            'id': 1,
            'username': 'updateduser',
            'email': 'updateduser@example.com'
        }
        response = self.app.patch('/users', json=updated_user)
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
