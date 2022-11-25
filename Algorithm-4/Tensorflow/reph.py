

# open poem.txt , separate sentences by punctuation, and save to new_poem.txt with each sentence on a new line
import re
import string

punclist = ['.', '!', '?']

# open poem.txt
with open('poem.txt', 'r') as f:
    # read poem.txt
    poem = f.read()
    # separate sentences by punctuation
    poem = re.sub(r'([.!?])', r' \1', poem)
    # save to new_poem.txt with each sentence on a new line
    with open('new_poem.txt', 'w') as f:
        f.write(poem)

# open new_poem.txt
with open('new_poem.txt', 'r') as f:
    # read new_poem.txt
    poem = f.read()
    # create empty string
    new_poem = ''
    # loop through poem and add each character to new_poem until a punctuation mark is reached
    for char in poem:
        if char not in punclist:
            new_poem += char
        else:
            new_poem += char + '\n'
    # save to new_poem.txt with each sentence on a new line
    with open('new_poem1.txt', 'w') as f:
        f.write(new_poem)

