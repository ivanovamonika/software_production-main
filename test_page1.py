from Page1 import Page1
import unittest
import tkinter as tk
import App as app


class TestPage1(unittest.TestCase, app):
    def testFileChosen(self):
        page = Page1(self.app)

        page.selectedFilePath = "house_zipcode_usa.csv"

        self.assertTrue(page.isFileChosen())

    def test_file_not_chosen(self):
        page = Page1(self.app)
        # Assert conditions
        self.assertFalse(page.isFileChosen())

if __name__ == '__main__':
    unittest.main(app)
