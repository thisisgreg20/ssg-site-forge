def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        count = len(line) - len(line.lstrip("#"))
        if count == 1:
            text = line.lstrip("#")
            return text.strip()
    raise Exception("no title found")
