import unittest
from htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main()