# copied from 'alice.py' into 'word_count.py'
# make my counting words code into a function so I can use it for more .txt files if I need to find out how many words
                                                                                            # are in any i need checked
from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
        # encoding arg is needed when the system default encoding doesn't match the encoding of the file that's being read
            # most likely will happen when reading from a file that wasn't created on your system
    except FileNotFoundError:
        print(f"\nSorry, the file {path} does not exist.\n")
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

