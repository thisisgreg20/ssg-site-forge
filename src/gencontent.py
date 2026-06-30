import os
from pathlib import Path
from block_markdown import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        count = len(line) - len(line.lstrip("#"))
        if count == 1:
            text = line.lstrip("#")
            return text.strip()
    raise Exception("no title found")

def get_file_contents(path):
    with open(path) as file:
        return file.read()
    
def write_file_contents(path, contents):
    if os.path.dirname(path) != "":
        os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as file:
        file.write(contents)
    
def generate_page(from_path, template_path, dest_path, base_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = get_file_contents(from_path)
    template = get_file_contents(template_path)
    html_node = markdown_to_html_node(markdown)
    title = extract_title(markdown)
    html_content = html_node.to_html()
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_content)
    template = template.replace("href=\"/", f"href=\"{base_path}")
    template = template.replace("src=\"/", f"src=\"{base_path}")
    write_file_contents(dest_path, template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path):
    file_list = os.listdir(dir_path_content)
    for file in file_list:
        source_path = os.path.join(dir_path_content, file)
        destination_path = os.path.join(dest_dir_path, file)
        if os.path.isdir(source_path):
            generate_pages_recursive(source_path, template_path, destination_path, base_path)
            continue
        if file[-3:] == ".md":
            p = Path(destination_path)
            destination_path = p.with_suffix(".html")
            generate_page(source_path, template_path, destination_path, base_path)


