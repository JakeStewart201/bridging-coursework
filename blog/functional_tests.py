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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Jake\'s Blog', header_text)

        #Finds a list of blog posts
        posts = self.browser.find_element_by_class_name('col-md-8')

        #Selects one to open
        post = posts.find_element_by_class_name('post')

        #Clicks on it
        post.find_element_by_tag_name('a').click()

        #Is directed to the blog post to read it
        self.assertTrue(self.browser.current_url.startswith('http://localhost:8000/post/'))


if __name__ == "__main__":
    unittest.main(warnings='ignore')
