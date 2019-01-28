from unittest.mock import patch

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='carben@gmail.com', password="password"):
    """ creates a sample user """
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """ Testing email and password functionality """
        email = "carlos@gmail.com"
        password = "123dev"
        user = get_user_model().objects.create_user(
            email=email, password=password
        )

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
        user = get_user_model().objects.create_superuser(
            "test@gmail.com", "lolpass"
            )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """ Test the tag string representation """
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Mexican'
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """ Test the ingredient string representation """
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name="Carrot"
        )

        self.assertEqual(str(ingredient), ingredient.name)

    def test_recipe_str(self):
        """ Test the recipe string representation """
        recipe = models.Recipe.objects.create(
            user=sample_user(),
            title="Steak and eggs",
            time_minutes=20,
            price=25.00
        )

        self.assertEqual(str(recipe), recipe.title)

    @patch('uuid.uuid4')
    def test_recipe_file_name_uuid(self, mock_uuid):
        """ Test that image is saved in correct location """
        uuid = "test-uuid"
        mock_uuid.return_value = uuid
        file_path = models.recipe_image_file_path(None, 'myimage.jpg')

        exp_path = f'uploads/recipe/{uuid}.jpg'
        self.assertEqual(file_path, exp_path)
