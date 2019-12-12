from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'azim1203@gmail.com'
        password = '092100027h'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        # hasilnya supposed to dalam assert ni
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(
            email,
            'test123'
        )

        # hasilnya supposed to dalam assert ni
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                None,
                'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'azim1203@gmail.com',
            '092100027h'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
