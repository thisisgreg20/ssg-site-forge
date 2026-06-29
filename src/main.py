import os
import shutil

def copy_src_to_destination(source: str = "./static", destination: str = "./public"):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.makedirs(destination)
    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)
        if os.path.isdir(source_path):
            print(f"Creating Directory: {destination_path}")
            copy_src_to_destination(source_path, destination_path)
        else:
            print(f"Copying File: {destination_path}")
            shutil.copy(source_path, destination_path)
            
def main() -> None:
    copy_src_to_destination()

if __name__ == "__main__":
    main()