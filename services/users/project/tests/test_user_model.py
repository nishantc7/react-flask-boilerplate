import unittest
from sqlalchemy.exc import IntegrityError
from project import db
from project.api.models import User
from project.tests.base import BaseTestCase
from project.tests.utils import add_user


class TestUserModel(BaseTestCase):

    def test_add_user(self):
        user = add_user('nishant', 'nishant@gmail.com')
        self.assertTrue(user.id)
        self.assertEqual(user.username, 'nishant')
        self.assertTrue(user.active)

    def test_add_duplicate_username(self):
        add_user('nishant', 'nishant@gmail.com')
        duplicate_user = User(
            username='nishant',
            email='nishant2@test.com'
            )
        db.session.add(duplicate_user)
        self.assertRaises(IntegrityError, db.session.commit)

    def test_to_json(self):
        user = add_user('nishant', 'nishant@gmail.com')
        self.assertTrue(isinstance(user.to_json(), dict))


if __name__ == '__main__':
    unittest.main()
