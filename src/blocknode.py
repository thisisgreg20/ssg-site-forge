from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED = "unordered_list"
    ORDERED = "ordered_list"
   
def block_to_block_type(block):
    if block.startswith("```") and block.endswith("```"):
        if "\n" in block:
            return BlockType.CODE
    lines = block.split("\n")
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        if len(lines) == 1:
            return BlockType.HEADING
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED
    is_ordered = True
    for i, line in enumerate(lines):
        expected_start = f"{i + 1}. "
        if not line.startswith(expected_start):
            is_ordered = False
            break
    if is_ordered:
        return BlockType.ORDERED
    return BlockType.PARAGRAPH