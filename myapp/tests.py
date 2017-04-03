from django.test import TestCase
from django.core.urlresolvers import resolve, reverse
from . import views

# Create your tests here.
class PageTest(TestCase):
    """All Pages Should:
    1. Resolve to the proper views
    2. Return a 200
    3. Use appropriate template
    4. Contain proper context data
    """
    fixtures = []

    def test_homepage(self):
        """
        Test the company URL and View
        """
        url = reverse('myapp:home')
        v = resolve(url)
        self.assertEqual(v.func.__name__,views.HomeView.__name__)
        response = self.client.get(url)
        self.assertEqual (response.status_code,200)
        self.assertTemplateUsed(response,'myapp/home.html')

    def test_about_page(self):
        """
        tests about page

        """
        url = reverse('myapp/about.html')
        v = resolve(url)
        self.assertEqual(v.func.__name__,views.AboutView.__name__)
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'myapp/about.html')
