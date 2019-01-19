from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """ Testing email and password functionality """
        email = "carlos@gmail.com"
        password = "123dev"
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ test email for new user is normalized """
        email = "carlos@Gmail.cOm"
        user = get_user_model().objects.create_user(email, "lol")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Test creation of user with no email raises error """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test1233")

    def test_create_new_super_user(self):
        """ Test creating a new super user """
        user = get_user_model().objects.create_superuser("test@gmail.com", "lolpass")

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

