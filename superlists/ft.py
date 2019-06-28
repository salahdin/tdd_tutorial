from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    # runs before any test runs
    def setUp(self):
        b = r'/Users/salahdinzeberga/PycharmProjects/mylasttry/superlists/geckodriver'
        self.browser = webdriver.Firefox(executable_path=b)
        self.browser.implicitly_wait(3)  # telling selenium to wait 3 sec if needed
    def tearDown(self): # runs before test is over
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('finish the test')  # fails no matter what , we are only using to display a message on here


if __name__ == '__main__':
    unittest.main(warnings='ignore')