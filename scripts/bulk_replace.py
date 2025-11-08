
import sys
import glob

def bulk_replace(old_string, new_string):
    for filepath in glob.iglob('**/*.md', recursive=True):
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        if old_string in content:
            new_content = content.replace(old_string, new_string)
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Replaced '{old_string}' with '{new_string}' in {filepath}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python bulk_replace.py <old_string> <new_string>")
        sys.exit(1)
    
    old_string = sys.argv[1]
    new_string = sys.argv[2]
    bulk_replace(old_string, new_string)
