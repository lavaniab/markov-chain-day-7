"""Generate Markov text from text files."""

# from random import choice
# # file_path = green-eggs.read()


# def open_and_read_file(file_path):
#     """Take file path as string; return text as string.

#     Takes a string that is a file path, opens the file, and turns
#     the file's contents as one string of text.
#     """
#     contents = open(file_path).read()
   
#     words = contents.split()
#     first_dict = {}
   
#     for idx in range(len(words) - 2):
       
#         key_variables = (words[idx], words[idx + 1], )
#         first_dict[key_variables] = first_dict.get(key_variables, [])
#         first_dict[key_variables].append(words[idx + 2])
        
#     # print(first_dict)
#     # contents.close()
#     return str(first_dict)

# text_string = "Would you could you in a house? Would you could you with a mouse?"
def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    Make a new key out of the second word in the first key and the random word
    you pulled out from the list of words that followed it.
    Look up that new key in the dictionary, and pull a new
    random word out of the new list.
    Keep doing that until your program raises a KeyError.
    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:
    (each tuple in our string is a list of all possible tuples)
        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    text_list = []
    
    chains_dict = {}

    text_string = text_string.split()
    for text in text_string:
        text_list.append(text)

    for idx in range(len(text_list) - 2):
        key_variables = (text_list[idx], text_list[idx + 1], )
        chains_dict[key_variables] = chains_dict.get(key_variables, [])
        chains_dict[key_variables].append(text_list[idx + 2])
    print(chains_dict)
    return chains_dict


make_chains('text_string')

# def make_text(chains):
#     """Return text from chains."""

#     words = []

#     # your code goes here

#     return " ".join(words)


# input_path = "green-eggs.txt"

# # Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print(random_text)
