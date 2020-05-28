import unittest
from sqlalchemy.exc import IntegrityError
from project import db
from project.api.models import User
from project.tests.base import BaseTestCase
from project.tests.utils import add_user


class TestUserModel(BaseTestCase):

    def test_add_user(self):
        user = add_user('nishant', 'nishant@gmail.com', 'over9000')
        self.assertTrue(user.id)
        self.assertEqual(user.username, 'nishant')
        self.assertTrue(user.active)
        self.assertTrue(user.password)

    def test_add_duplicate_username(self):
        add_user('nishant', 'nishant@gmail.com', 'over9000')
        duplicate_user = User(
            username='nishant',
            email='nishant2@test.com',
            password='over9000'
        )
        db.session.add(duplicate_user)
        self.assertRaises(IntegrityError, db.session.commit)

    def test_to_json(self):
        user = add_user('nishant', 'nishant@gmail.com', 'over9000')
        self.assertTrue(isinstance(user.to_json(), dict))

    def test_passowrds_are_random(self):
        user_one = add_user('testing', 'test@test.com', 'over9000')
        user_two = add_user('testing2', 'test@test2.com', 'over9000')
        self.assertNotEqual(user_one.password, user_two.password)


if __name__ == '__main__':
    unittest.main()
