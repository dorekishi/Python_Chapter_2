from pathlib import Path
from word_count import count_words

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

for fn in filenames:
    path = Path(fn)
    count_words(path)

# if i write pass for the exception block, the code will keep going and not output anything