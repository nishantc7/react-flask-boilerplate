import json
import unittest
from project.tests.base import BaseTestCase
from project.tests.utils import add_user


class TestUserService(BaseTestCase):
    """Tests for the Users Service."""

    def test_users(self):
        """Ensure the /ping route behaves correctly."""
        response = self.client.get('/users/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])

    def test_add_user(self):
        """Ensure a new user can be added to database"""
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({
                    'username': 'nishant',
                    'email': 'nishant@testmail.com'
                }),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('nishant@testmail.com was added', data['message'])
            self.assertIn('success', data['status'])

    def test_add_user_invalid_json(self):
        """Error thrown if JSON empty"""
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({}),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])
            self.assertIn('fail', data['status'])

    def test_add_user_invalid_key(self):
        """Ensure error thrown if JSON doesn't have username key"""
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({
                    'email': 'nishant@email.com'
                }),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])
            self.assertIn('fail', data['status'])

    def test_add_duplicate_user(self):
        """Ensure error if user already exists"""

        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({
                    'username': 'nishant',
                    'email': 'nishant@testmail.com'
                }),
                content_type='application/json',
            )
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({
                    'username': 'nishant',
                    'email': 'nishant@testmail.com'
                }),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('That email already exists.', data['message'])
            self.assertIn('fail', data['status'])

    def test_single_user(self):
        """Try to get single user"""
        user = add_user('nishant', 'nishant@gmail.com')
        with self.client:
            response = self.client.get(f'/users/{user.id}')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('nishant', data['data']['username'])
            self.assertIn('nishant@gmail.com', data['data']['email'])
            self.assertIn('success', data['status'])

    def test_single_user_incorrect_id(self):
        """Ensure error is thrown if the id does not exist."""
        with self.client:
            response = self.client.get('/users/999')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('User does not exist', data['message'])
            self.assertIn('fail', data['status'])

    def test_all_users(self):
        """Ensure all users list works"""
        add_user('nishant', "nishant@email.com")
        add_user('rick', "rick@email.com")
        with self.client:
            response = self.client.get('/users')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data['data']['users']), 2)
            self.assertIn('nishant', data['data']['users'][0]['username'])
            self.assertIn('rick', data['data']['users'][1]['username'])
            self.assertIn('success', data['status'])


if __name__ == '__main__':
    unittest.main()
