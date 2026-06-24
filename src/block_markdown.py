def markdown_to_blocks(markdown):
    doc = markdown.split("\n\n")
    blocks = []
    for block in doc:
        block = block.strip()
        if not block:
            continue
        blocks.append(block)
    return blocks