import re
import sys

def clean_text(text):
    # Extra spaces aur special characters saaf karne ka tool
    text = re.sub(r'\s+', ' ', text).strip()
    return text

if __name__ == "__main__":
    sample = "   Hello    World!   Clean   this   text.  "
    print("Cleaned Output:", clean_text(sample))
