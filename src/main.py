import sys
from copystatic import copy_src_to_destination
from gencontent import generate_pages_recursive

def main() -> None:
    if len(sys.argv) > 1:
        base_path = sys.argv[1]
    else:
        base_path = "/"
    copy_src_to_destination()
    generate_pages_recursive("./content/", "./template.html", "./docs/", base_path)
    

if __name__ == "__main__":
    main()