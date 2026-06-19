from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    text_test = TextNode("this is a cat", TextType.BOLD, "www.google.com")
    print(f"\n{text_test}")

    html_test_node = HTMLNode("h1", "hello world", None, {"background": "black", "fontcolor": "red", "fontsize": "12"})
    html_test = html_test_node.props_to_html()
    print(f"\nHTML Node Props Test: {html_test}\n")

main()