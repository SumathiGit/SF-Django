from django.test import TestCase
import django.contrib.auth
from salesforce.testrunner.example.models import Account


class WebTest(TestCase):
    databases = '__all__'

    def test_admin(self):
        """Test that mainly improves code coverage."""

        # Log in as a superuser
        user = django.contrib.auth.models.User.objects.create_user('admin', 'sumathi0251@gmail.com', 'sumathi')
        user.is_superuser = True
        user.is_staff = True
        user.save()
        self.client.login(username='admin', password='sumathi')

        account = Account(Name='sf_test account')
        account.save()

        response = self.client.get('/')
        response = self.client.get('/search/')
        response = self.client.post('/search/', {'query': 'test account'})
        self.assertIn(b'sf_test account', response.content)
        response = self.client.post('/admin/example/account/')
        response = self.client.post('/admin/example/contact/')
        response = self.client.post('/admin/example/lead/')
        response = self.client.post('/admin/example/pricebook/')
        response = self.client.post('/admin/')
        self.assertIn('PricebookEntries', response.rendered_content)
        account.delete()
        user.delete()
