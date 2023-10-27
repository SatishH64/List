import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    # Initialize webdriver
    def setUp(self):
        self.browser = webdriver.Firefox()

    # Test Cases
    def test_todo_list_start(self):
        # Homepage of the website
        self.browser.get("http://localhost:8000")

        # Check title of Webpage
        self.assertIn("To-Do", self.browser.title)

        # This fails always
        self.fail("Finish Test!")

        # Quit Webdriver

    def tearDown(self):
        self.browser.quit()


# Checks if imported or executed from command line
if __name__ == "__main__":
    unittest.main()
