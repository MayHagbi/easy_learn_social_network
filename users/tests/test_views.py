from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from users.models import Profile


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

        self.view_profile_url = reverse('users:view_profile')
        self.edit_profile_url = reverse('users:edit_profile')

        # create user
        self.username = 'testuser'
        self.email = 'test@test.com'
        self.password = '12345'
        self.user = User(username=self.username, email=self.email)
        self.user.set_password(self.password)
        self.user.save()
        login = self.client.login(username=self.username, password=self.password)
        self.assertEqual(login, True)

        # create profile
        self.profile = Profile.objects.create(
            user=self.user,
            birth_date='1999-1-1',
            gender='male',
            college_name='SCE',
            year_of_study='3',
            about_me='some text'
        )

    def test_test_view(self):
        assert 1 == 1

    def test_view_profile_view(self):
        response = self.client.post(self.view_profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/profile.html')

    def test_edit_profile_view(self):
        response = self.client.post(self.edit_profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/edit_profile.html')