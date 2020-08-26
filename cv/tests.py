from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from blog.views import cv

class CVPageTest(TestCase):

    def test_cv_url_resolves_to_cv_view(self):
        found = resolve('/cv')
        self.assertEquals(found.func,  cv)

    def test_cv_returns_correct_html(self):
        request = HttpRequest()
        response = post_list(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('\n<html>'))
        self.assertIn('<title>Jake\'s CV</title>', html)
        self.assertTrue(html.endswith('</html>\n'))
