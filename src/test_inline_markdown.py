import unittest
from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter

class TestInlineMarkdown(unittest.TestCase):
    def test_split_code(self):
        node = TextNode("This has `code` inside", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This has ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "code")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertEqual(new_nodes[2].text, " inside")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)

    def test_split_bold(self):
        node = TextNode("This is **very important** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[1].text, "very important")
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)

    def test_does_not_split_non_text_nodes(self):
        node = TextNode("This has `code` but is already bold", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0], node)

if __name__ == "__main__":
    unittest.main()