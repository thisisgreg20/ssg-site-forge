import unittest
from htmlnode import HTMLNode,LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_multi(self):
        test_control_text = ' background="black" fontcolor="red" fontsize="12"'
        node = HTMLNode("h1", "hello world", None, {
            "background": "black",
            "fontcolor": "red",
            "fontsize": "12"
        })
        node_props = node.props_to_html()
        self.assertEqual(test_control_text, node_props)
    
    def test_props_to_html_none(self):
        test_control_text = ""
        node = HTMLNode("p", "hello world", None, None)
        node_props = node.props_to_html()
        self.assertEqual(test_control_text, node_props)

    def test_props_to_html_empty(self):
        test_control_text = ""
        node = HTMLNode("h5", "hello world", None, {})
        node_props = node.props_to_html()
        self.assertEqual(test_control_text, node_props)

    def test_leafnode_to_html_empty(self):
        test_control_text = "<p>This is a paragraph of text.</p>"
        node = LeafNode("p", "This is a paragraph of text.", {})
        node_to_html = node.to_html()
        self.assertEqual(test_control_text, node_to_html)

    def test_leafnode_to_html_with_props(self):
        test_control_text = '<a href="http://www.google.com">This is a link to google.</a>'
        node = LeafNode("a", "This is a link to google.", {"href": "http://www.google.com"})
        node_to_html = node.to_html()
        self.assertEqual(test_control_text, node_to_html)
    
    def test_leafnode_to_html_with_props_not_eq(self):
        test_control_text = '<a href="http://www.boot.dev">This is a link to Boot.Dev.</a>'
        node = LeafNode("a", "This is a link to google.", {"href": "http://www.google.com"})
        node_to_html = node.to_html()
        self.assertNotEqual(test_control_text, node_to_html)

if __name__ == "__main__":
    unittest.main()