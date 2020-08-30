from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from cv.views import cv_page

class CVPageTest(TestCase):

    def test_cv_url_resolves_to_cv_view(self):
        found = resolve('/cv')
        self.assertEquals(found.func,  cv_page)

    def test_cv_returns_correct_html(self):
        request = HttpRequest()
        response = cv_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('\n<html>'))
        self.assertIn('<title>Jake\'s CV</title>', html)
        self.assertTrue(html.endswith('</html>\n'))
