from textnode import TextNode, TextType

def main():
    text_test = TextNode("this is a cat", TextType.BOLD, "www.google.com")
    print(text_test)

main()