from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import TextNode, TextType
from blocknode import BlockType, block_to_block_type

def markdown_to_blocks(markdown):
    doc = markdown.split("\n\n")
    blocks = []
    for block in doc:
        block = block.strip()
        if not block:
            continue
        blocks.append(block)
    return blocks

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        