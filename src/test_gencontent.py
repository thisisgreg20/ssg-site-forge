import unittest
from gencontent import extract_title

class TestGenContent(unittest.TestCase):
    def test_extract_title_eq(self):
        md = """
This is **bolded** paragraph
text in a p
# Heading here

This is another paragraph with _italic_ text and `code` here

"""
        heading = extract_title(md)
        self.assertEqual(heading, "Heading here")

    def test_extract_title_eq2(self):
        md = """
This is **bolded** paragraph
text in a p
#Heading 1 here      

This is another paragraph with _italic_ text and `code` here

"""
        heading = extract_title(md)
        self.assertEqual(heading, "Heading 1 here")
    
    def test_extract_title_exception_check(self):
        md = """
This is **bolded** paragraph
text in a p
###### Heading 6 here

This is another paragraph with _italic_ text and `code` here

"""
        with self.assertRaises(Exception):
            extract_title(md)