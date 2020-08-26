from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_open_a_blog_post(self):
        self.browser.get('http://localhost:8000/cv')

        self.assertIn('Jake\'s CV', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Jake\'s CV', header_text)

        self.fail('Finish rest of test')

if __name__ == "__main__":
    unittest.main(warnings='ignore')
