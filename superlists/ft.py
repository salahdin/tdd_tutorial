from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
        #user browses to out page
        self.browser.get(' http://127.0.0.1:8000/')

        # header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        # self.fail('finish the test')  # fails no matter what , we are only using to display a message on here

        # using method selenium provides that finds elements of an html by the tag name to capture the header text
        header_text =  self.browser.find_element_by_tag_name('h1').text
        # assertIn returns true if To-do is in the headers
        self.assertIn('To-do', header_text)

        # user finds a tab to add new to-do
        # capture an html element by the id
        inputbox = self.browser.find_element_by_id('id_new_item')

        # if the place holder of the html input field is the same as the second argument return true
        self.assertAlmostEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
        self.fail('end of test')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
