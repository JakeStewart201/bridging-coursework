from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.contrib.auth import get_user_model

from cv.views import cv_page

class CVPageTest(TestCase):
    
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user('temp', 'temp@gmail.com', 'temp')

    def test_cv_url_resolves_to_cv_view(self):
        found = resolve('/cv/')
        self.assertEquals(found.func,  cv_page)

    def test_cv_returns_correct_html(self):
        request = HttpRequest()
        response = cv_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('\n<html>'))
        self.assertIn('<title>Jake\'s CV</title>', html)
        self.assertTrue(html.endswith('</html>\n'))

    def test_cv_uses_cv_template(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'cv/cv_page.html')

    def test_can_save_an_interest_POST_request(self):
        User = get_user_model()
        self.client.login(username='temp', password='temp')

        response = self.client.post('/edit_interest/', data={'name':'test','importance':'100','text':'test text'}, follow=True)

        self.assertIn('test text', response.content.decode())
        self.assertTemplateUsed(response, 'cv/cv_page.html')


    def test_can_redirect_an_interest_POST_request(self):
        User = get_user_model()
        self.client.login(username='temp', password='temp')

        response = self.client.post('/edit_interest/', data={'name':'test','importance':'100','text':'test text'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cv/')
