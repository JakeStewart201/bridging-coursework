from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_open_a_blog_post(self):
        #Opens the homepage
        self.browser.get('http://localhost:8000')
        #Reads the header
        self.assertIn('Jake\'s Blog', self.browser.title)
        self.fail('Finish the test!')
        #Finds a list of blog posts
        #Selects one to open
        #Clicks on it
        #Is directed to the blog post to read it
