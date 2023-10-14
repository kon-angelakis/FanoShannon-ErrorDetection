#-----Fano-Shannon compression-----#

"""
chars_dict and chars_list have the following structure:
   [ Character, [ Probability, PartitionState(T/F), [ BinaryCompression ] ] ]
"""

from libs.compression import partition, compress
from collections import Counter


def FanoShannon():
    f = open("./text.txt", "r")
    data = f.read()
    f.close()

    raw_data = list(data.strip(""))
    chars_dict = Counter()

    # Count every character in raw_data and append it in this dictionary
    chars_dict.update(raw_data)

    # Calculate the probabilities and update chars_dict with probability, partitioning state, and bit encoding
    length = len(raw_data)
    for char, count in chars_dict.items():
        chars_dict[char] = [count / length, False, []]
    chars_dict = dict(sorted(chars_dict.items(), key = lambda x:x[1], reverse = True)) #sort the dictionary
   
    #Turn the dictionary into a list for easy access
    chars_list = [[[char] + [prob]] for char, prob in chars_dict.items()]
    partition(chars_list)

    compressed_data = compress(raw_data, chars_dict) #list
    compressed_data = ''.join([str(elem) for elem in compressed_data]) #binary string

    return compressed_data

FanoShannon()