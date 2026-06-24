import unittest
from blocknode import BlockType, block_to_block_type

class TestBlockToBlockType(unittest.TestCase):

    def test_paragraph(self):
        block = "This is a normal paragraph of text with no special markdown symbols at the start."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_heading_valid(self):
        # Test distinct heading levels 1 to 6
        self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("### Heading 3"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Heading 6"), BlockType.HEADING)

    def test_heading_invalid(self):
        # Missing space after hash symbols makes it a paragraph
        self.assertEqual(block_to_block_type("##Heading"), BlockType.PARAGRAPH)
        # More than 6 hashes makes it a paragraph
        self.assertEqual(block_to_block_type("####### Heading 7"), BlockType.PARAGRAPH)

    def test_code_block_valid(self):
        block = "```\ndef my_func():\n    return True\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_code_block_invalid(self):
        # Missing leading newline or closing backticks
        self.assertEqual(block_to_block_type("``` python code ```"), BlockType.PARAGRAPH)

    def test_quote_block_valid(self):
        block = "> This is a quote\n> spanning multiple lines\n>with or without space"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_quote_block_invalid(self):
        # One line is missing the '>' character
        block = "> This is a quote\n Missing character here\n> End of quote"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_unordered_list_valid(self):
        block = "- Item 1\n- Item 2\n- Item 3"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED)

    def test_unordered_list_invalid(self):
        # Missing a space after the dash on the second line
        block = "- Item 1\n-Item 2\n- Item 3"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_list_valid(self):
        block = "1. First item\n2. Second item\n3. Third item"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED)

    def test_ordered_list_invalid_start(self):
        # Must start exactly at 1
        block = "2. First item\n3. Second item"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_list_invalid_increment(self):
        # Sequence must increment smoothly by 1
        block = "1. First item\n3. Second item"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()