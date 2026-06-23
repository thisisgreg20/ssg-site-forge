import unittest
from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links

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

    def test_extract_images(self):
        text = "This is an image ![boots](https://boot.dev/wizard_bear.png)"
        matches = extract_markdown_images(text)
        # We expect a list containing one tuple: (alt_text, url)
        self.assertEqual(matches, [("boots", "https://boot.dev/wizard_bear.png")])

    def test_extract_links(self):
        text = "Check out [Boot.dev](https://www.boot.dev) for more magic."
        matches = extract_markdown_links(text)
        self.assertEqual(matches, [("Boot.dev", "https://www.boot.dev")])

    def test_extract_multiple(self):
        text = "Link [one](url1) and link [two](url2)"
        matches = extract_markdown_links(text)
        self.assertEqual(matches, [("one", "url1"), ("two", "url2")])

    def test_no_false_positives(self):
        # The Link extractor should NOT catch images
        text = "This is an image ![alt](url)"
        matches = extract_markdown_links(text)
        self.assertEqual(len(matches), 0)

    def test_relative_links(self):
        text = "Go to [About](/about-us)"
        matches = extract_markdown_links(text)
        self.assertEqual(matches, [("About", "/about-us")])

if __name__ == "__main__":
    unittest.main()