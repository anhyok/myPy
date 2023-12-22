class UserDatabase:
    def __init__(self):
        self.users = {"user1": "password1", "user2": "password2"}

    def get_password(self, username):
        return self.users.get(username)

class Authenticator:
    def __init__(self, user_database):
        self.user_database = user_database

    def authenticate(self, username, password):
        correct_password = self.user_database.get_password(username)
        return password == correct_password

import unittest

class TestUserAuthentication(unittest.TestCase):
    def setUp(self):
        user_database = UserDatabase()
        self.authenticator = Authenticator(user_database)

    def test_successful_authentication(self):
        self.assertTrue(self.authenticator.authenticate("user1", "password1"))

    def test_failed_authentication(self):
        self.assertFalse(self.authenticator.authenticate("user1", "wrong_password"))

if __name__ == '__main__':
    unittest.main()
