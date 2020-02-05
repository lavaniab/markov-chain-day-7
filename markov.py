"""Generate Markov text from text files."""

from random import choice
# file_path = green-eggs.read()

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    contents = open(file_path).read()
    # read_file = open_file.read()
    # print(read_file)
    # read_file = str(read_file)
    # print(read_file)
    words = contents.split()
    first_dict = {}
    # appended_dict = {}
    
    # key_value_paired = []

    # key_variables = [(words[word], words[word + 1], )]
    for idx in range(len(words) - 2):
        # if word in words:
        # value_list = [words[idx]]
        key_variables = (words[idx], words[idx + 1], )
        # first_dict[key_variables] = value_list
    # print(first_dict)
        # if key_variables in words:
        first_dict[key_variables] = first_dict.get(key_variables, [])
        first_dict[key_variables].append(words[idx + 2])
        # print(value_list)
            # appended_dict[key_variables] = value_list.append(word) 
            # print(appended_dict)
        # else:
        #  first_dict[key_variables] = value_list.append(words[word]) # dict obj has no attr 'append'
        # for key_variables in words:
        #     appended_dict[words[word], words[word + 1]] = value_list.append([words[word] + (words[word])])            
        #new_tuples = (words[word], words[word + 1])
        # # print(new_tuples)
        # for new_tuples in first_dict:
        # import pdb; pdb.set_trace()
        # first_dict = {(words[word], words[word + 1]) : words[word+2]}
    # print(value_list)
    print(first_dict)
    # print(value_list)
    # for new_tuples in words:
    #     first_dict = 
    # loop through our list of words, append any value that corresponds to each 
    # key value as a list for each key
    return str(first_dict)


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
