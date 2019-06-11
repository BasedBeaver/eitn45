from itertools import groupby
from heapq import *
import math


class Node(object):
    left = None
    right = None
    char = None
    freq = 0

    def __init__(self, c, f):
        self.char = c
        self.freq = f

    def set_children(self, ln, rn):
        self.left = ln
        self.right = rn

    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, Node):
            return False
        return self.freq == other.freq


def code_tree(x, node):
    if node.char:
        if not x:
            codes[node.char] = "0"
        else:
            codes[node.char] = x
    else:
        code_tree(x + "0", node.left)
        code_tree(x + "1", node.right)


def distribution_entropy(prob_list):
    entropy = 0
    for prob in prob_list:
        entropy -= prob * math.log(prob, 2)
    return entropy


def get_total_freq(node_list):
    total_freq = 0
    for node in node_list:
        total_freq += node.freq
    return total_freq


def probability_list(node_list):
    total_freq = get_total_freq(node_list)
    p_list = []
    for node in node_list:
        p_list.append(node.freq / total_freq)
    return p_list


def avg_codeword(nbr_bits_coded, nbr_bytes_uncoded):
    return nbr_bits_coded/nbr_bytes_uncoded


def percentages_bits(bit_string):
    total = 0
    ones = 0
    for bit in bit_string:
        total += 1
        if bit == "1":
            ones += 1
    return (total-ones)/total, ones/total


def distribution(node_list):
    dist_list = []
    for node in node_list:
        dist_list.append((chr(node.char), node.freq))
    return dist_list


str_alice = open('alice29.txt', 'rb').read()  # Read in file.txt byte-wise.
item_nodes = [Node(a, len(list(b))) for a, b in groupby(sorted(str_alice))]
prob_list = probability_list(item_nodes)
dist_list = distribution(item_nodes)


# Use built in heapq algorithm to make life easier and implement the simple huffman-tree algorithm
heapify(item_nodes)
while len(item_nodes) > 1:
    left = heappop(item_nodes)
    right = heappop(item_nodes)
    n = Node(None, right.freq+left.freq)
    n.set_children(left, right)
    heappush(item_nodes, n)

# Debug / checking correctness
for node in item_nodes:
    print("Root node freq: ", node.freq)  # Combined freq is 152089 as per problem description

codes = {}
code_tree("", item_nodes[0])
corrected_codes = {chr(k): v for k, v in codes.items()}  # Change representation of keys from ASCII to chars
coded_alice = "".join([codes[a] for a in str_alice])  # Code alice.txt with the Huffman-coding
percentages_zeros, percentages_ones = percentages_bits(coded_alice)

print("\nCharacter distribution: ", sorted(dist_list, key=lambda x: x[1], reverse=True))
print("\nCharacter encodings: \n", corrected_codes, "\n")
print("Length of compressed alice.txt in bytes: ", len(coded_alice)/8)  # Divide by 8 due to bits to bytes
print("Average codeword length: ", avg_codeword(len(coded_alice), len(str_alice)))
print("Entropy of distribution: ", distribution_entropy(prob_list))
print("\nTotal number of bits in coded alice: ", len(coded_alice))
print("Percentage of zeros: ", percentages_zeros)
print("Percentage of ones: ", percentages_ones)
