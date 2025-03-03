from pathlib import Path
####
# this segment was created after writing the code before and after the hashes surrounding this
# i made this just to make sure my code worked for counting the number of words in the alice.txt file
p = Path('alice.txt')
p.write_text(f"Hello World")
####
path = Path('alice.txt')
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