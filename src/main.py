from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    text_test = TextNode("this is a cat", TextType.BOLD, "www.google.com")
    print(text_test)

    html_test = HTMLNode("h1", "hello world", None, {
        "background": "black",
        "fontcolor": "red",
        "fontsize": "12"
    })
    print(html_test)

main()