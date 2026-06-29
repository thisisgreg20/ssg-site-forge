from enum import Enum
from htmlnode import ParentNode
from textnode import TextType, TextNode, text_node_to_html_node
from inline_markdown import text_to_textnodes

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        block = block.strip()
        if block == "":
            continue
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    if block_type == BlockType.OLIST:
        return ordered_list_to_html_node(block)
    if block_type == BlockType.ULIST:
        return unordered_list_to_html_node(block)
    raise ValueError("invalid block type")

def text_to_children(text):
    textnodes = text_to_textnodes(text)
    htmlnodes = []
    for textnode in textnodes:
        htmlnodes.append(text_node_to_html_node(textnode))
    return htmlnodes

def paragraph_to_html_node(markdown: str) -> ParentNode:
    lines = markdown.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line.strip())
    text = " ".join(new_lines)
    children = text_to_children(text)
    return ParentNode("p", children)

def heading_to_html_node(markdown: str) -> ParentNode:
    count = len(markdown) - len(markdown.lstrip("#"))
    text = markdown[count + 1:]
    children = text_to_children(text)
    return ParentNode(f"h{count}", children)

def code_to_html_node(markdown: str) -> ParentNode:
    textnode = TextNode(markdown[4:-3], TextType.TEXT)
    htmlnode = text_node_to_html_node(textnode)
    codenode = ParentNode("code", [htmlnode])
    return ParentNode("pre", [codenode])

def quote_to_html_node(markdown: str) -> ParentNode:
    lines = markdown.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line.lstrip(">").strip())
    text = " ".join(new_lines)
    children = text_to_children(text)
    return ParentNode("blockquote", children)

def unordered_list_to_html_node(markdown: str) -> ParentNode:
    lines = markdown.split("\n")
    li_nodes = []
    for line in lines:
        li_nodes.append(ParentNode("li", text_to_children(line[2:])))
    return ParentNode("ul", li_nodes)

def ordered_list_to_html_node(markdown: str) -> ParentNode:
    lines = markdown.split("\n")
    li_nodes = []
    for line in lines:
        li_nodes.append(ParentNode("li", text_to_children(line.split(". ", 1)[1])))
    return ParentNode("ol", li_nodes)