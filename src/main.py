from copystatic import copy_src_to_destination
from gencontent import generate_pages_recursive

def main() -> None:
    copy_src_to_destination()
    generate_pages_recursive("content/", "template.html", "public/")
    

if __name__ == "__main__":
    main()