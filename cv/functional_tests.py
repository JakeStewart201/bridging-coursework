from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_read_cv(self):
        #Opens cv
        self.browser.get('http://localhost:8000/cv')

        #Sees that it's the cv in the title
        self.assertIn('Jake\'s CV', self.browser.title)

        #Sees the title for the CV
        header_text = self.browser.find_element_by_class_name('active').text
        self.assertIn('CV', header_text)

        #Can read education history
        education = self.browser.find_element_by_id('education')
        qualifications = education.find_elements_by_class_name('qualification')
        self.assertTrue(
            any(qualification.find_element_by_class_name('institution').text == 'University of Birmingham' for qualification in qualifications)
        )

        #Can read employment history
        employment_history = self.browser.find_element_by_id('employment_history')
        jobs = employment_history.find_elements_by_class_name('job')
        self.assertTrue(
            any(job.find_element_by_class_name('employer').text == "Barnardo’s Charity Shop" for job in jobs)
        )

        #Can read skills
        skill_list = self.browser.find_element_by_id('skills')
        skills = skill_list.find_elements_by_class_name('skill')
        self.assertTrue(
            any('Python' in skill.text for skill in skills)
        )

        #Can read interests
        interest_list = self.browser.find_element_by_id('interests')
        interests = interest_list.find_elements_by_class_name('interest')
        self.assertTrue(
            any('climbing' in interest.text for interest in interests)
        )

        #Can read projects
        project_list = self.browser.find_element_by_id('projects')
        projects = project_list.find_elements_by_class_name('project')
        self.assertTrue(
            any('Quaker Royale' in project.find_element_by_class_name('name').text for project in projects)
        )


if __name__ == "__main__":
    unittest.main(warnings='ignore')
